class minHeap:
    # Index:  [0, 1, 2, 3, 4, 5]
    # Value: [3, 8, 5, 10, 9, 7]
    """
    Tree Representation:
        3
       / \
      8   5
     / \ /
    10 9 7

    #main 
    """

    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i-1)//2
    
    def right_child(self, i):
        return 2*i + 2
    
    def left_child(self, i):
        return 2*i + 1
    
    def insert(self, key):
        self.key.append(key)

    def heapify(self, i):
        