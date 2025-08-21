# Thread-safe artifact store
"""
Implement a thread-safe ArtifactStore class with put(artifact_id, data) 
and get(artifact_id) methods, 
ensuring concurrent access doesn’t corrupt data.
"""
from threading import Lock

class ArtifactStore:
    def __init__(self):
        self.store = {}
        self.lock = Lock()

    def put(self, artifact_id, data):
        with self.lock:
            self.store[artifact_id] = data

    def get(self, artifact_id):
        with self.lock:
            return self.store.get(artifact_id)