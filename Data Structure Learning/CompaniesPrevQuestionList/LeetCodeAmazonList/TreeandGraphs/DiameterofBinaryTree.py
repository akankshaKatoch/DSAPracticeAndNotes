# Definition for a binary tree node.
from typing import Optional

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdepth = 0

        def depth(node):
            if not node: return 0

            leftdepth = depth(node.left)
            rightdepth = depth(node.right)

            self.maxdepth = max(self.maxdepth, leftdepth +rightdepth)

            return 1 + max(leftdepth, rightdepth)
        depth(root)
        return self.maxdepth

