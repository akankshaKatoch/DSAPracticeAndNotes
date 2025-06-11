from collections import deque
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = TreeNode()
#       1
#      / \
#     2   3
#    / \
#   4   5
# Breadth First search output will be -> [1,2,3,4,5]
# we will access values from each breadth and print it. 
# we will use queue data structure for it. 
# BFS Traversal dont have any recursive implementation. 
# Under the hood recusive function have stack call therefore it wont for BFS search. 

    def BFSSearch(self, root):
        if not root: return []
        
        queue = deque([root])
        result = []
        #enter first element in q remove it checkfor child add athe the end and remove from the front

        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            

        return result





    

