# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Is basically travesal and creating a string of the nodes. 
        def inorder(node):
            if not root:
                return "null,"
            
            
            return str(node.val)+ ',' + inorder(root.left) + inorder(root.right)
        return inorder(root)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #now to deserialise we need to split the node into list 
        nodeList = data.split(',')
        self.i = 0

        def dfs():
            if nodeList[self.i] == 'null':
                self.i += 1
                return None
            node = TreeNode(val=nodeList[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
