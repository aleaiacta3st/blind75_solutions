def isValidBST(node):
    def dfs(node,lower_bound,upper_bound):
        if node is None:
            return True 
        if node.val>lower_bound and node.val<upper_bound:
            return dfs(node.left,lower_bound,node.val) and dfs(node.right,node.val,upper_bound)
    return dfs(node,-float('inf'),float('inf'))


# BST Validation Logic: The Narrowing Boundaries Approach
# Recursively check each node against progressively narrowing value boundaries. 
# Each node passes its own value as a new boundary to its children - 
# becoming the upper bound for left children and lower bound for right 
# children. Start with infinite boundaries at the root.
            
#without ranges, if you just compare a node with its children, you are missing
# the case where a node deep down the tree violates the rules of a bst
# that is why we need to enforce a range    