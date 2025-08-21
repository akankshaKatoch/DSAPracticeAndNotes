# 13) Quick “Idempotent Ingest” Sketch (by checksum)

import hashlib

class ArtifactStore:
    """Name+version+sha256; dedupe by sha; O(1) ops (avg)."""
    def __init__(self):
        self.by_sha = {}        # sha256 -> (name, version)
        self.meta = {}          # (name, version) -> sha256

    def put(self, name: str, version: str, data: bytes) -> bool:
        sha = hashlib.sha256(data).hexdigest()
        if sha in self.by_sha:  # idempotent
            self.meta[(name,version)] = sha
            return False  # duplicate content
        self.by_sha[sha] = (name, version)
        self.meta[(name,version)] = sha
        return True

    def get_sha(self, name: str, version: str) -> str | None:
        return self.meta.get((name,version))
