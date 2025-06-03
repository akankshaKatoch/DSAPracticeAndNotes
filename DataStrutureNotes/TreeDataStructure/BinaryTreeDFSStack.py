class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, root, node):
        if not root:
            root = node
            return root
        
    """
      1
     / \
    2   3
   / \
  4   5
    "Pre order travelsal o/p : 1, 2, 4, 5, 3"
    """
        
    def depthFirstSearchpreorder(self, root):
        result = []
        if not root: 
            return result
        stack = [root]
        "Pre order travelsal o/p : 1, 2, 4, 5, 3"
        while len(stack)>0:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)   
            result.append(node.value)
        return result
    
    """
         1
        / \
       2   3
      / \
     4   5
    "In-order travelsal o/p : 4, 2, 5, 1, 3"
    """

    def depthfirstsearchinorder(self, root):
        #inorder logic o/p : left root right: we will keep pushing all left nodes first  
        if not root:
            return []
        current = root
        stack = []
        result = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            # stack = [1,2,4]
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    """
         1
        / \
       2   3
      / \
     4   5
    "post-order travelsal o/p : 4, 5,2,3,1"
    left -> right -> root
    """

    def depthfirstsearchpostoder(self, root):
        #inorder logic o/p : left root right: we will keep pushing all left nodes first  
        if not root:
            return []
        current = root
        stack = []
        result = []
        last_visited = None
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else: 
                peek = stack[-1]
                if peek.right and peek.right != last_visited:
                    stack.append(peek.right)
                else: 
                    last_visited = stack.pop()
                    result.append(peek.value)
        return result