from collections import deque
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node) -> None:
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add_to_back(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        node.prev = prev
        self.tail.prev = node

    def _move_to_back(self, node: Node) -> None:
        self.remove(node)
        self._add_to_back(node)       

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_back
        return node.val 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_back(node)
            return 
        node = Node(key,value)
        self.cache[key] = node
        self._add_to_back(node)

        if len(self.cache)>self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    
        
    
        




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)