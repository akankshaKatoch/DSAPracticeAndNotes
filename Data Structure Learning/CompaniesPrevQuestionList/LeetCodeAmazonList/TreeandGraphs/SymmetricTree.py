# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

        def checkValue(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            return (node1.val == node2.val and checkValue(node1.left, node2.right) and checkValue(node1.right, node2.left))
        

        return checkValue(root.right, root.left)