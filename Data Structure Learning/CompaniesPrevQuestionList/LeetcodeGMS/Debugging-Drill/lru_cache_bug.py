class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class LRUCache:
    """Least Recently Used cache.
    Bug(s):
    - get() returns value but doesn't move to head.
    - put() evicts when size == capacity (off-by-one) and may drop wrong node.
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        # BUG: should move to head to mark recent
        return node.v

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.v = value
            # BUG: also move to head
            return
        node = Node(key, value)
        self.map[key] = node
        self._add_front(node)
        if len(self.map) >= self.cap:  # BUG: should evict when > cap
            # evict LRU (node before tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
