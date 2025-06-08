"""For LRU cache we need to keep certain things in mind.
1st It should be fixed in capacity. 
2nd as name indicates least recently used item is evicted first. 
3rd we get value based on key.

We have to think of the solution where we update whatever is recently used.
I can think of the deque -> add recently used item at front and back will have least recently used item.
For faster fetch we can have hash map for the key. """



class Node:
    def __init__(self, key=0,val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        #hashmap to maintain key value.
        self.cache = {}
        #Nodes to maintain 1st and last element to indicate the tail and head all elements are in between
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addHead(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node


    def removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev       

    def get(self, key: int) -> int:
        # to implement this check in dict or hashmap if present remove from the nodes and add at the front. 
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addHead(node)
            return node.val
        return -1    

    def put(self, key: int, value: int) -> None:
        # Now put method to put new element in the LRU means adding key-value in dict and 
        # removing least used value which will be from the end of the node. and adding to the head. 

        # if key already there it simple as get its moved to front. 
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.addHead(node)
        # if key is not there remove the tail element if ache is full and add at the head of the linked list
        else: 
            if len(self.cache) == self.capacity:
                lruNode = self.tail.prev
                self.removeNode(lruNode)
                del self.cache[lruNode.key]
            #add new node
            newNode = Node(key,value)
            self.cache[key] = newNode
            self.addHead(newNode)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)