from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.max_bst_size = 0
        def dfs(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'))

            left_is_bst, left_size, left_min, left_max = dfs(node.left)
            right_is_bst, right_size, right_min, right_max = dfs(node.right)

            # If current node's subtree is BST
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                size = left_size + right_size + 1
                self.max_bst_size = max(self.max_bst_size, size)
                return (True, size, min(node.val, left_min), max(node.val, right_max))
            else:
                return (False, 0, 0, 0)

        dfs(root)

        return self.max_bst_size

        