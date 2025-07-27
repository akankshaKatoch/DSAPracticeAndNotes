# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        newNode = TreeNode(root.val)

        newNode.left = self.invertTree(root.right)
        newNode.right = self.invertTree(root.left)

        return newNode


