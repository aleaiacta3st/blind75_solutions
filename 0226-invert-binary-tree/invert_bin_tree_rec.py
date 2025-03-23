def invertTree(root):
    if not root:
        return root 
    if (root.left==None and root.right==None):
        return root 
    else:
        root.left,root.right=root.right,root.left
        invertTree(root.left)
        invertTree(root.right)
    return root
    