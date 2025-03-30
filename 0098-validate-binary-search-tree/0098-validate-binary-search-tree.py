# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def dfs(node, last_seen_value):
        #     if node is None:
        #         return True
            
        #     # Traverse left subtree first
        #     if not dfs(node.left, last_seen_value):#goes down all the way to the left
        #         return False
            
        #     # Check current node against last seen value
        #     if node.val <= last_seen_value: #then check current node
        #         return False
            
        #     # Traverse right subtree with updated last seen value
        #     return dfs(node.right, node.val) #update last seen and check right tree
        
        # return dfs(root, float('-inf'))





# Syntax error: def dfs(node.left, ...) is invalid Python. 
# Parameter names can't include dot notation.'
# ''
# 'Reach the leftmost and carry back its value'
# ' while rising up'
# ''

# There's no fixed relationship between the number of arguments a '
# 'function takes and the number of values it can return as a tuple in Python.'
# ''
# 'Your function might receive a single scout (the node) as an argument, '
# 'yet return a detailed map and battle assessment - '
# 'a tuple of (is_valid, last_value).'

# node.val <= last_seen_value:
# the leftmost leaf should pass the test, hence we compare it against -infinity


# e choose -float('inf') (negative infinity) as the initial value for a very specific reason: to ensure the leftmost node in the tree passes the comparison test regardless of what value it contains.
# Here's why this is essential:
# In a valid BST, an inorder traversal produces values in ascending order
# The leftmost node is the first node we'll check in our inorder traversal
# We need that first node to be validated against something, but we don't '
# 'want to restrict what value it can have

# By using negative infinity as our initial comparison value, we're essentially '
# 'saying: "The first node we process must be greater than negative infinity" - '
# 'which is true for any real number. This allows our BST to contain any values, '
# 'even extremely negative ones, as long as they maintain the correct ordering '
# 'relative to each other.
# If we had used a different value like 0 or -1000, we would incorrectly reject 
# valid BSTs that happen to have values below that threshold.
# This approach maintains the true essence of the BST property: it's about '
# 'the relative ordering of nodes, not their absolute values.



# How to Think About Recursion in Tree Problems
# The art of creating recursive functions like this comes down to a 
# few key concepts:

# Trust the recursion. This is the hardest part. 
# When you write dfs(node.left, last_seen_value), you need to trust that it 
# will completely solve the left subtree before proceeding.

# Think about information flow. In tree recursion, information typically flows:
# Down the tree through parameters (like passing last_seen_value)
# Back up through return values

# Start with the base case. Always begin by asking "When does the recursion "
# "stop?" For trees, it's usually when we hit null nodes.'
# ''
# 'The last_seen_value update happens through parameter passing, not variable '
# 'assignment. When we call dfs(node.right, node.val), '
# 'we're passing the current node's value as the new minimum threshold '
# 'for the entire right subtree.'
# ''

# Practical Approach to Recursive Functions
# I recommend this process:
# Define what your function should return (boolean for Valid BST)
# Identify the base case (null node returns True)
# Figure out what information needs to flow (the minimum allowed value)
# Trust that your recursive calls work for subtrees

# The helper dfs should return True if the subtree rooted at node satisfies
# the BST property relative to last_seen_value.
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
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