# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True 
        if p==None or q==None:
            return False
        if (p.val==q.val):
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False


# In Python:
# None is the Python keyword that represents the absence of a value.
# null does not exist. 


# Tree P
#     1
#    / \
#   2   3

# Tree Q 
#     1
#    / \
#   2   3


# isSameTree(1,1)
#    ├── isSameTree(2,2)
#    │       ├── isSameTree(None,None) → True
#    │       └── isSameTree(None,None) → True
#    └── isSameTree(3,3)
#            ├── isSameTree(None,None) → True
#            └── isSameTree(None,None) → True
        