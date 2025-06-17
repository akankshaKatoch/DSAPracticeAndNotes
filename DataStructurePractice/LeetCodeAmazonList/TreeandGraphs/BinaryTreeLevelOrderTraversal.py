# Definition for a binary tree node.
from typing import List 
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: 
            return []
        result = []

        que = deque()
        deque.append([root])
        #[[1], [9, 20], [15, 17]
        while que:
            levelsize = len(que)
            levelList = []

            for _ in range(levelsize):
                currNode = que.popleft()
                levelList.append(currNode.val)

                if currNode.left:
                    que.append(currNode.left)
                if currNode.right:
                    que.append(currNode.right)
            result.append[levelList]

        return result
        
        