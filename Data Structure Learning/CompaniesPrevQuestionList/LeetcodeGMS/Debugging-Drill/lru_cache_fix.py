class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class LRUCache:
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

    def _move_to_front(self, node):
        self._remove(node)
        self._add_front(node)

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        self._move_to_front(node)
        return node.v

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._move_to_front(node)
        else:
            node = Node(key, value)
            self.map[key] = node
            self._add_front(node)
            if len(self.map) > self.cap:
                lru = self.tail.prev
                self._remove(lru)
                del self.map[lru.k]
