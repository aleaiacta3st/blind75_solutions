# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        global_max=[0]

        
        def postorder(node):
            if not node:
                return 0
            left=postorder(node.left)
            right=postorder(node.right)
            global_max[0]=max(global_max[0],left+right)
            return 1+max(left,right)
            
        postorder(root)

        return global_max[0]
