class TreeNode:
    def __init__(self, value= 0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right 

class Tree: 
    def __init__(self, root):
        self.node = TreeNode()
    # inorder left -> root > Right
    def inorderrecursiveSearch(self, root):
        if not root:
            return []
        result = []
        def inorder(root, result):
            if not root:
                return None
            if root.left:
                inorder(root.left, result)
            result.append(root.value)
            if root.right:
                inorder(root.right, result)
        inorder(root, result)
        return result
       
    # preorder left -> root > Right
    def preorderrecursiveSearch(self, root):
        if not root:
            return []
        result = []
        def preorder(root, result):
            if not root:
                return None
            result.append(root.value)
            if root.left:
                preorder(root.left, result)
            if root.right:
                preorder(root.right, result)
        preorder(root, result)
        return result
       

    # Postorder:  left -> right -> root
    def postorderrecursiveSearch(self, root):
        if not root:
            return []
        result = []
        def postorder(root, result):
            if not root:
                return None 
            if root.left:
                postorder(root.left, result)
            if root.right:
                postorder(root.right, result)
            result.append(root.value)
        postorder(root, result)
        return result  
        