# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p is None or q is None:
            return None 
        def dfs(node):
            if node is None:
                return None 
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            elif p.val>node.val and q.val>node.val:
                return dfs(node.right)
            else:
                return node 
        return dfs(root)
        