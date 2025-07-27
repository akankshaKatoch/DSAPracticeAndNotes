# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node):
            if not node:
                return 0
            
            leftHeight = check_height(node.left)
            if leftHeight == -1:
                return -1
            
            right_height = check_height(node.right)
            if right_height == -1:
                return -1 
            if abs(leftHeight-right_height) > 1:
                return -1
            return max(leftHeight,right_height) + 1

        return check_height(root) != -1
        