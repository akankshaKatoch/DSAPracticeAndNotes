# 12) Simple Sliding-Window Rate Limiter (per key)

from collections import deque
import time

class RateLimiter:
    """Allow at most 'limit' events per 'window' seconds per key. O(1) amortized."""
    def __init__(self, limit: int, window: float):
        self.limit = limit
        self.window = window
        self.events = {}  # key -> deque[timestamps]

    def allow(self, key: str, now: float = None) -> bool:
        now = time.time() if now is None else now
        dq = self.events.setdefault(key, deque())
        # evict old
        cutoff = now - self.window
        while dq and dq[0] <= cutoff:
            dq.popleft()
        if len(dq) < self.limit:
            dq.append(now)
            return True
        return False
