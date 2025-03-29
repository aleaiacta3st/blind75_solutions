# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,lower_bound,upper_bound):
            if node is None:
                return True 
            if node.val>lower_bound and node.val<upper_bound:
                return dfs(node.left,lower_bound,node.val) and dfs(node.right,node.val,upper_bound)
            else:
                return False
        return dfs(root,-float('inf'),float('inf'))