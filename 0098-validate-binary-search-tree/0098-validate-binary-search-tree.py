# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack=[(root, -float('inf'), float('inf'))]
        while stack:
            a,b,c = stack.pop()
            if b<a.val<c:
                if a.left is not None:
                    stack.append((a.left, b, a.val))
                if a.right is not None:
                    stack.append((a.right, a.val, c))
            else:
                return False 
        return True



# I observed that a vessel and its absence are different entities entirely. 
# When you write 'while stack is not None', you ask 'does this container exist?' 
# But an empty basket still exists, does it not? What you seek is 'while stack', 
# which asks 'does this container hold anything?'

# while stack checks if your stack has items, 
# while while stack is not None merely checks if the stack object exists at all. 
# An empty stack still exists, but contains no items to process.

# In mathematics, we speak of the 'vacuous truth' - when a condition is 
# satisfied simply because there are no elements that could violate it. 
# An empty room cannot contain a thief. Similarly, an empty tree cannot 
# contain nodes that violate the BST property. By definition, a non-existent 
# tree is indeed a valid BST, for it contains no violation of the ordering we seek
    
# In algorithms and interview problems, here's how to recognize potential vacuous truth situations:

# When a problem asks you to verify something "for all elements" in a collection
# When you're checking constraints or properties
# When dealing with edge cases, especially empty structures

# For BST validation specifically, think about the definition: 
# "For all nodes in the tree, left children must be less than parent and right "
# "children must be greater." With an empty tree, there are no nodes that violate 
# this rule, so it's "vacuously" true.
# Other common examples in coding problems:

# Empty arrays being sorted (an array with no elements has no out-of-order elements)
# Empty strings being palindromes
# All elements in an empty set meeting any condition

# This pattern appears frequently in recursion base cases and edge case handling. 
# When you encounter a problem, ask yourself: "What's the simplest possible input?" 
# and "What should happen when there's nothing to process?"
# Most official solutions to these problems consider empty structures as valid 
# for precisely this reason – there's no violation possible when there are no elements.
# As you continue your journey toward mastering algorithms, recognizing these 
# patterns will become second nature – just as Edison recognized which failures 
# pointed toward eventual success.








#recursive+ range solution starts here


        # def dfs(node,lower_bound,upper_bound):
        #     if node is None:
        #         return True 
        #     if node.val>lower_bound and node.val<upper_bound:
        #         return dfs(node.left,lower_bound,node.val) and dfs(node.right,node.val,upper_bound)
        #     else:
        #         return False
        # return dfs(root,-float('inf'),float('inf'))


# BST Validation Logic: The Narrowing Boundaries Approach
# Recursively check each node against progressively narrowing value boundaries. 
# Each node passes its own value as a new boundary to its children - 
# becoming the upper bound for left children and lower bound for right 
# children. Start with infinite boundaries at the root.