# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum = float('-inf')
        #calculate max path using dfs for right and left
        def dfs_max_path(node):
            if not root:
                return 0
            
            left_sum = dfs_max_path(root.left)
            right_sum = dfs_max_path(root.right)
            current_sum = node.val + left_sum + right_sum 
            self.sum = max(self.sum, current_sum)
            return node.val + max(left_sum, right_sum)
        
        dfs_max_path(root)
        return self.sum
            