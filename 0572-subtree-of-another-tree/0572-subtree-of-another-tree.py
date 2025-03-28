# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False 
        def isSameTree(p,q):
            if p==None and q==None:
                return True 
            if p==None or q==None:
                return False
            if (p.val==q.val):
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
            return False
        
        def dfs(root):
            if root is None:
                return False
            if isSameTree(root,subRoot):
                return True 
            return dfs(root.left) or dfs(root.right)

        return dfs(root)


# The proper base case for this function is simply:
#     if root is None:
#     return False
# This signifies you've reached the end of a '
# 'branch without finding your target -

# short-circuit evaluation.'
# This means that if dfs(root.left) evaluates to True, 
# then indeed, dfs(root.right) will not be evaluated at all

# n coding terms, this OR logic means: 
# 'If we find the subtree match anywhere in the '
# 'left branch, return True immediately (and stop searching). '
# 'Otherwise, check the right branch.' T
        