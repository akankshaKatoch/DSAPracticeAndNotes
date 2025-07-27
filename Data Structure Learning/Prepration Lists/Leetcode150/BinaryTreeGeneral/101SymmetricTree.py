# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def checkValues(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            return ((node1.val == node2.val) and checkValues(node1.left, node2.right) and checkValues(node1.right, node2.left))
        
        return checkValues(root.right, root.left)
        
