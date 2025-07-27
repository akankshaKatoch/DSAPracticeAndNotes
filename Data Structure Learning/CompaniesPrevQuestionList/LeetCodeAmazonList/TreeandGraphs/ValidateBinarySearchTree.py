# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validcheck(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low <node.val < high):
                return False
        
            return (validcheck(node.left,low, node.val) and validcheck(node.right, node, high))
        
            

        return validcheck(root) 

     