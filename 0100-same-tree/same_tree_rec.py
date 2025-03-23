def isSameTree(p,q):
    if p==None and q==None:
        return True 
    if p==None or q==None:
        return False
    if (p.val==q.val):
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
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

