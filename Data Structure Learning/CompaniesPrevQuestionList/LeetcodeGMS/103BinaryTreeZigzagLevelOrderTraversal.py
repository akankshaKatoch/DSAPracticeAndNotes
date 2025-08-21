from typing import Optional, List
from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        stack = deque([root])
        left_to_right = True
        while stack:
            levelList = deque()
            levelSize = len(stack)
            for i in range(levelSize):
                currNode = stack.popleft()
                if left_to_right:
                    levelList.append(currNode.val)
                else:
                    levelList.appendleft(currNode.val)
                
                if currNode.left:
                    stack.append(currNode.left)
                if currNode.right:
                    stack.append(currNode.right)

            result.append(list(levelList))
        return result


        