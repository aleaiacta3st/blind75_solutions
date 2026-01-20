# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """


        def dfs(node):
            if not node:
                return ["null"]
            return [str(node.val)] + dfs(node.left) + dfs(node.right)

        return ",".join(dfs(root))

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tokens=data.split(",")
        index=0

        def build():
            nonlocal index
            if tokens[index]=="null":
                index=index+1
                return None 
            curr=TreeNode(int(tokens[index]))
            index=index+1
            curr.left=build()
            curr.right=build()
            return curr 

        return build()
            
            


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))