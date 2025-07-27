# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root: return 0

        self.sum = float('-inf')

        def dfs_max(node):
            if not node:
                return 0
            
            leftsum = dfs_max(node.left)
            rightsum = dfs_max(node.right)

            cur_sum = leftsum+rightsum+node.val
            self.sum = max(cur_sum, self.sum)

            return node.val + max(leftsum,rightsum)
        
        dfs_max(root)
        return self.sum




        