from collections import deque
class TreeNode:
    def __init__(self,value, left= None, right= None):
        self.value= value
        self.left = left
        self.right = right

# For normal insertion in binary tree we dont use any comaprision. 
# Just look for the first available position and insert node. 
# Add nodes at first available point. 

class Tree:
    def __init__(self):
        self.root = TreeNode

    def insertionInTree(self, root, value):
        newNode = TreeNode(value)
        if not root:
            return newNode

        queue = deque([root])

        while queue:
            curr = queue.popleft()
            if not curr.left:
                curr.left = newNode
                return root
            else: 
                queue.append(curr.left)
            if not curr.right:
                curr.right = newNode
                return root
            else: 
                queue.append(curr.right)
        return root


                

