class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.right = right
        self.left = left

class Tree:
    def __init__(self):
        self.node = TreeNode
    # recusrion
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(root, maxSoFar):
            if not root:
                return 0
            
            count = 1 if root.value>=maxSoFar else 0
            newMax = max(maxSoFar, root.value)

            count += dfs(root.left, newMax)
            count += dfs(root.right, newMax)

            return count  
        return dfs(root, float('-inf'))
    
    #stack
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, float('-inf'))]
        count = 0

        while stack:
            curr, maxsofar = stack.pop()
            count = max(count, curr.value)
            if curr.value >= maxsofar:
                count += 1
            if curr.left:
                stack.append(curr.left)
        
