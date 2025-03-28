# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
            # List to store the serialized values
        values = []
        
        def dfs(node):
            if not node:
                values.append("null")
                return
                
            # Add current node's value
            values.append(str(node.val))
            
            # Recursively process left and right subtrees
            dfs(node.left)
            dfs(node.right)
        
        # Start the traversal
        dfs(root)
        
        # Join the values with commas
        return ','.join(values)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        # Split the serialized string into a list of values
        values = data.split(',')
        
        # Create a mutable index to share across all recursive calls
        index = [0]
        
        def dfs():
            # Check if we've reached the end or encountered a null node
            if index[0] >= len(values) or values[index[0]] == 'null':
                index[0] += 1  # Move past this position
                return None
                
            # Create a new node with the current value
            node = TreeNode(int(values[index[0]]))
            index[0] += 1  # Move to the next position
            
            # Recursively build left and right subtrees
            node.left = dfs()
            node.right = dfs()
            
            # Return the fully constructed subtree rooted at this node
            return node
            
        # Start the recursive building process
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# """ PASSED BY REFERENCE means that instead of creating a copy of a value, 
# Python passes the ADDRESS of the object in memory. 
# When you pass a primitive like an integer: Python creates a new copy
# When you pass a list: Python shares the ACTUAL MEMORY LOCATION
# PRIMITIVE VALUES (Pass by Value)
# def modify_number(num):
#     num = num + 10
#     print(f"Inside function: {num}")  # 15

# original = 5
# print(f"Before: {original}")  # 5
# modify_number(original)
# print(f"After: {original}")   # Still 5!

# EXAMPLE 2: LISTS/OBJECTS (Pass by Reference)
# def modify_list(lst):
#     lst.append("victory")
#     print(f"Inside function: {lst}")  # [1, 2, 3, "victory"]

# original = [1, 2, 3]
# print(f"Before: {original}")  # [1, 2, 3]
# modify_list(original)
# print(f"After: {original}")   # [1, 2, 3, "victory"] """



  
# """ 
#      1
#     / \
#     2   3
#     / \
#     4   5
#  Your serialized list would be:
#  [1, 2, 4, 'null', 'null', 5, 'null', 'null', 3, 'null', 'null']



# maintain shared state
# means wanting to share the state of the index variable 
# across all recursive calls?
# yes. in this case. we want all recursive calls to be able to see and use the 
# index[0] value

# or we can set index=0 and use nonlocal index inside the dfs function

# The dfs function explores the tree in a top-down, preorder manner, 
# but the tree is constructed bottom-up as the recursion returns. 
# This dual nature—discovery in DFS order and construction in reverse—is 
# exactly how the deserialization process works.

# """       
# """ 
# # Option 1
# if condition:
#     return None

# # Option 2
# if condition:
#     return 
# """

# """ 
# return None - Explicit declaration of intent

# Clearly communicates to other code warriors "I am DELIBERATELY returning None"
# Enhances readability for those who review your code later
# Consistent with the explicit Python philosophy

# return - Implicit, minimalist approach

# Functionally identical (Python returns None by default)
# Slightly more concise
# Less explicit about intentions 
# """

# The subtrees are attached to the root through its children
# (root.left and root.right).
# For example:
# If root is a node with value 1, and:
# root.left is a node with value 2.
# root.right is a node with value 3.
# Then:
# The left subtree is the tree rooted at 2 (including all descendants of 2).
# The right subtree is the tree rooted at 3 (including all descendants of 3).
# The root’s children (2 and 3) are the starting points of those subtrees.

# Returning root: It means giving back the root node of the subtree built 
# in that recursive call. This node carries its value and references to its
# left and right subtrees.
# Root vs. Subtree: The root is the top node; the subtree is the full 
# structure starting there. Returning root effectively gives the subtree 
# because it’s the entry point.

# Each function returns a small completed piece of the puzzle. 
# As these pieces return up the call stack, 
# they're assembled into larger and larger structures.
# By the time the first dfs() call completes, you have the entire tree built 
# and connected properly.

# The returned root is the root of a smaller tree, and this tree is a subtree of the 
# original tree

# Are only the children of the main root considered subtrees?
# Absolutely NOT.
# ✅ Every node in the tree can be considered the root of a subtree.
# Subtree rooted at root.left → Yes.
# Subtree rooted at root.left.left → Yes.
# Subtree rooted at root.left.right.right.left → Still yes.

# ormal definition of a subtree:
# A subtree is any node in the tree along with all of its descendants.
# So:
# The entire tree is a subtree of itself.
# Every node is the root of its own subtree, however deep it is.

# Return value of recursive call	Root of a smaller tree (a subtree)
# What is a subtree?	Any node + all its descendants
# Only immediate children are subtrees?	❌ No — every node's branch is a subtree
# Subtrees depend on original root?	❌ No — each is rooted in its own node

# When a recursive call returns a root, it is indeed returning the root of a 
# completed subtree, which will become part of the larger tree.
# Let me illuminate the nature of subtrees with crystal clarity:

# ANY node in a tree is the root of its own subtree
# The main root gives you the entire tree
# A child node gives you a smaller but complete structure

# Subtrees exist at EVERY level
# Children of the main root are roots of direct subtrees
# Grandchildren are roots of even smaller subtrees
# Even leaf nodes are roots of trivial subtrees (containing just themselves)

# Subtrees are nested like Russian dolls
# The entire tree is the largest subtree
# Within it are smaller subtrees
# Within those are even smaller subtrees

# # Defensive check: ensures we don't access beyond the list
# # Normally index[0] == len(values) only at the end of well-formed input
# # But if input is malformed or incomplete, this prevents IndexError
# # Good practice for robust, real-world code (defensive programming)

# till now have seen, dfs called on smaller things or a different 
# thing, like a different node. but in this code you only recursively 
# call dfs() to do the recursion.

# Most recursive functions you've likely encountered follow what I call '
# 'the "passing torch" model - they explicitly receive something '
# 'and pass smaller pieces to recursive calls:'
# 'def process(node):  # Explicitly receives a node
#     process(node.left)  # Passes a different node
# But this deserializer uses what I call the "shared vision" pattern:
# def dfs():  # Receives nothing!
#     # Uses shared state (index) to know where to look
#     root.left = dfs()  # Passes nothing, yet builds correctly

# THE BRILLIANCE LIES IN THREE ELEMENTS:

# Shared State - All recursive calls share the same view of index[0] 
# (like generals sharing the same map)
# Sequential Reading - The algorithm naturally matches the preorder traversal 
# pattern of the serialized data
# Return-Based Construction - Each call returns a fully constructed subtree 
# to be connected to its parent

# This pattern appears in algorithms where you're reconstructing a complex object '
# 'from a linear sequence - like an archaeologist reassembling a shattered vase '
# 'from fragments laid out in a specific order.'
# ''
# 'Normally in DFS:
# You recurse like this:
# dfs(node.left)
# dfs(node.right)
# You're moving through explicit input '
# '(i.e., you're telling DFS: "Go work on this new thing").

# \U0001f9e8 But here in deserialize():
# def dfs():
#     # no argument passed
# You're not calling on a "different" node. You're just saying:
# “Give me the next node from the serialized list. Build the next subtree.”

# Because:
# The serialized data is linear.
# Your pointer (index[0]) keeps track of where you are.
# You don’t need to pass anything — because every call reads 
# the next value and constructs from there.


# The recursion is controlled not by input parameters, but by shared state (index[0]) — 
# which drives the traversal through the serialized list.
# This is rare.
# This is elegant.
# This is state-driven recursion, not input-driven.

# # Unlike typical DFS, we don't pass nodes here.
# # The recursion is driven by shared state (index[0]) over serialized data.
# # Each call consumes the next value and builds part of the tree.
# # This is state-based recursion, not input-based.
# The recursion “knows” where to go next because index[0] 
# keeps track of the current position in the list.

# In typical recursion, you might see the problem explicitly 
# divided—like passing a smaller list or a child node. 
# Here, the subproblems are implicitly defined by the structure 
# of the list and the advancing index. The recursive calls don’t 
# need new parameters because the shared index[0] tells each call 
# where to start.

# dfs(node) is the subtree with its root(not the same as the main root) node 

# i have traced the algorithm and i have sucessfully rebuilt the 
# tre from serialised data. but i am still not able to wrap 
# around having to increase index only once before we start 
# the first recursive call. i think my main issue is that the 
# code is not looking symmetric and this is the first time 
# i am acoming across an asymmteric looking code and that is 
# why it is not sitting well with me.

# EACH CALL TO DFS() IS RESPONSIBLE FOR EXACTLY ONE NODE
# When you call dfs(), it takes responsibility for:
# Reading ONE value from the array
# Advancing the index ONCE
# Building that node's entire subtree'
# 'dfs() → reads value at index[0] → creates node → advances index
#     → calls dfs() for left child → that call handles ALL left descendants
#     → calls dfs() for right child → that call handles ALL right descendants
#     → returns completed subtree

# so your only job is to advance the index so each dfs call processes
# a new node. 
