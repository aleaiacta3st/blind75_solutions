# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issameTree(p,q):
            if not p and q:
                return False
            if p and not q:
                return False
            if not p and not q:
                return True
            if p.val!=q.val:
                return False
            return issameTree(p.left,q.left) and issameTree(p.right,q.right)

        if not root and subRoot:
            return False
        if root and not subRoot:
            return False
        if not root and not subRoot:
            return True
        if root.val==subRoot.val:
            if issameTree(root,subRoot):
                return True
            else:
                return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        if root.val!=subRoot.val:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
            
        
        


        