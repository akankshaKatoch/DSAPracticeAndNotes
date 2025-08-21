from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if not root:
            return 0
        
        def pathfromroots(node, target):
            if not root: return 0

            count = 0

            if node.val == targetSum:
                count+=1
            count += pathfromroots(node.left, target - node.val)
            count += pathfromroots(node.right, target - node.val)

            return count

        pathsfromRoot = pathfromroots(root, targetSum)
        pathsfromLeftNode = pathfromroots(root, targetSum)
        pathfromrightNodes = pathfromroots(root, targetSum)

        return pathsfromRoot + pathfromrightNodes + pathsfromLeftNode
    
    def pathSumOpti(self, root: Optional[TreeNode], targetSum: int) -> int:

        prefixSum = defaultdict(int)

        prefixSum[0] = 1

        def pathfromroots(node, currSum):
            if not root: return 0

            count = 0
            currSum += node.val
            count = prefixSum[currSum - targetSum]
            prefixSum[currSum] += 1
            count += pathfromroots(node.left, currSum)
            count += pathfromroots(node.right, currSum)

            prefixSum[currSum] -= 1

            return count


        return pathfromroots(root, 0)



        