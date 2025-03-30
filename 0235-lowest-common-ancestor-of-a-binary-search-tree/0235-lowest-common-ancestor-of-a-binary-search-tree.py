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



# Major explanations lie in kthsmallest problem

# While writing the recursive function, don't think of the tree'
# Just think of the current node 
# Trust that the recursive call dfs(node.left) or dfs(node.right) works and that
# they will give you the answer you need
# and process only the current node. That is all you have to do. 

# When you do root.left - focus shifts - essentially we are traversing
# This is the movement that does not intuitively feel like a movement 
# In every recursive call, we are processing exactly one node. 
# We give every node as argument to the same piece of logic 

# Also observe that the values of p and q are hardcoded into the dfs function

#The LCA is where the split happens and the nodes went their separate ways
# If both values are less than the current node, shift focus to left and search 
# If both values are greater than the current node, shift focus to right and search
# If one is bigger and the other is smaller than the current node, you are at the LCA 
        