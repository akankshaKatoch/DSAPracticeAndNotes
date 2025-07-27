from collections import deque
from typing import List
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:   
        if not root:
            return []
        
        que = deque([root])
        #level = 1
        result = []
        left_to_right = True

        while que:
            levelSize = len(que)
            levelList = deque()
            for _ in range(levelSize):
                curr_node = que.popleft()
                if left_to_right: 
                    levelList.append(curr_node.val)
                else:
                    levelList.appendleft(curr_node.val)
        
                if curr_node.left:
                    que.append(curr_node.left)
                if curr_node.right:
                    que.append(curr_node.right)
            result.append(list(levelList))
            left_to_right = not left_to_right
                

        return result

