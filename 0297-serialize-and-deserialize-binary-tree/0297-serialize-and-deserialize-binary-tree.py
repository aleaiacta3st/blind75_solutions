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


# bfs approach starts here
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root:
#             return "[]"
#         serialized=[]
#         queue=deque([root])
#         while queue:
#             n=len(queue)
#             for i in range(n):
#                 popped_node=queue.popleft()
#                 if popped_node!=None:
#                     serialized.append(str(popped_node.val))
#                     queue.append(popped_node.left)
#                     queue.append(popped_node.right)
#                 else:
#                     serialized.append("null")
#         return "[" + ",".join(serialized) + "]"
                

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         if not data or data == "[]":
#             return None
#         data = data[1:-1].split(",")
#         root = TreeNode(int(data[0]))
#         parents_that_need_children_assigned=deque([root])
#         data_walker=0
#         while parents_that_need_children_assigned and data_walker<len(data):
#             popped_parent=parents_that_need_children_assigned.popleft()
#             if popped_parent is not None:
#                 if data_walker+1<len(data) and data[data_walker+1]!="null":
#                     popped_parent.left = TreeNode(data[data_walker+1])
#                     parents_that_need_children_assigned.append(popped_parent.left)
#                 if data_walker+2<len(data) and data[data_walker+2]!="null":
#                     popped_parent.right = TreeNode(data[data_walker+2])
#                     parents_that_need_children_assigned.append(popped_parent.right)
#             data_walker+=2
#         return root
        
    
# Serialize:
# Similar to level order traversal
# But here we want to include None as well 

# Deserialise:
# Create the root node from the first element of data 
# Create a queue which tracks the parents who need to have children assigned
# Pop from the queue 
# Assign children to it from data 
# Now children nodes are created 
# But they are not yet assigned children of their own yet 
# Queue them up 

# Additionally we also need to have a tracker which tracks which element in 
# the data list we are at.


# it is not that children are in the next two position of the popped node, 
# but the next 2 unassigned children are assigned to it.
# Exactly. In a BFS serialization, the parent’s own index in the data array 
# isn’t what determines where its children appear. Instead, there's a single '
# '"child pointer" or index that’s always advancing to the next unprocessed '
# 'child entries. Each parent, in the order it’s dequeued, receives the next '
# 'two unclaimed child entries from that pointer. Once assigned, the pointer '
# 'jumps past those two entries, ready for the next parent. So while it feels '
# 'like “popped node at index X has children at indices X+1 and X+2,” in 
# 'reality it’s “popped parent gets whatever two child spots come next '
# 'in the queue.”'

# if data[data_walker+1]
# if this is the only check, 0 in python is falsey. 
# so if the child’s value is actually zero, it won’t create that node. 
# The usual fix is to check for None rather than relying on truthiness:
# if data[data_walker + 1] is not None:


# The queue and data appear to be in sync but they may not be. 
# The queue may have parents with unassigned children while we have exhausted 
# the children that can be assigned in data. 
# So only while parents_that_need_children_assigned: is not enough 
# we need to have while queue and i < len(data):
# so that we stop looping when we hit the end of data 
# whatever nodes remaining in the queue are leaves 

# at the start of while loop, we did an index check,
# while processing each of the children also, we did an index check 
# isnt the first condition alone sufficient?
# no 
# the first check checks for i 
# it does not check for i+1 and i+2 inside the while loop also staying 
# within bounds 
# that is why both checks are necessary 

# Each BFS round: You pop one parent from the queue. 
# In an ideal world, you then read two child values from data 
# (one for the left child, one for the right). If they exist, 
# you attach them to the parent and enqueue those children.

# Truncation scenario: Now imagine the data does not have enough child entries 
# left to match the number of parents that remain in the queue. You’ll reach a 
# point where there are still nodes in the queue (each awaiting children), 
# but you’ve used up all your serialized data. If your code tries to read 
# another child from data at this point, it goes beyond the valid indices 
# and triggers an IndexError.

# The while i < len(data) check ensures you never enter the loop if you’ve 
# run out of data. Meanwhile, the individual checks inside the loop 
# protect against situations where you might do something like 
# data[i + 1] or data[i + 2] if you’re near the boundary. 
# Relying solely on try/except blocks or only checking inside the 
# loop can still let you into a situation where the loop itself is 
# active, but no valid data remains to process.

#  What is null vs. "null"?
# null (without quotes) doesn’t exist in Python.
# In Python, we use None.
# But in string output (like serialize() return), you must return a string. 
# You cannot return a Python object like None.
# So we represent None in the output by the string "null". 
# This is a LeetCode convention.
# ⚔️ Bottom line:
# Inside Python: None
# In output string: "null"

# What is ""?
# An empty string.
# If the tree is empty, we initially tried returning "". But LeetCode wants "[]" (an empty list in string form).
# So if root is None, you must return "[]" instead of "".
# ⚔️ Bottom line:
# Empty tree output: "[]" not "".

# 3️⃣ Why do we join by commas?
# Your serialized data needs to look like:
# [1,2,3,null,null,4,5]
# This means after converting every node or None into strings, 
# you join them with commas using:
# ",".join(serialized)

# 4️⃣ Why wrap it in brackets?
# eetCode doesn’t want just 1,2,3,null,null,4,5 — it wants:
# [1,2,3,null,null,4,5]
# So we put square brackets around that string using:
# "[" + ",".join(serialized) + "]"

# 5️⃣ During deserialization, what do we do with brackets?
# ou receive something like:
# "[1,2,3,null,null,4,5]"
# You cannot split this directly — it includes brackets.
# So you remove the first and last character:
# data = data[1:-1].split(",")
# This leaves you with: ["1", "2", "3", "null", "null", "4", "5"]
# And then you turn each "null" back into None in logic, or skip creating 
# children if it’s "null".

# What did you return in Level Order Traversal problem?
# In that problem, you:
# Traverse the tree level by level.
# Storethe val of each node in a list of lists (each inner list for one level).
# Finally, return a list of lists like:
# ➡️ You returned a Python data structure (list of lists).

# 2️⃣ What are we returning in serialize?
# LeetCode asks you to store the tree structure in a string form, 
# so that it can be easily transmitted/stored.
# Instead of returning a Python list or object,
# You flatten the tree level order into a list with None represented by "null",
# Then convert this whole list into a single string that looks like a list:
# "[1,2,3,null,null,4,5]"
# You are not just returning values. You’re returning a blueprint of the tree in string form.

# 3️⃣ Why return a string in serialize()?
# Imagine this as "saving" the tree.
# Python lists are Python objects — can’t easily transmit or store outside Python.
# Strings can be stored in databases, sent over networks, saved in files.
# The string has to contain all the structure (with nulls), not just values.
# That’s why serialize() returns a single string

# serialize() = "Save this tree into a string blueprint."
# deserialize() = "Take that blueprint string and rebuild the actual tree."

# Operation	Input	              Output
# Level Order	Tree	               List of lists (each list is values at one level)
# Serialize	Tree	                A single string that looks like a flattened tree: "[1,2,3,null,null,4,5]"
# Deserialize	That string blueprint	Reconstructed tree (root node of type TreeNode)




""" 
when you do level order traversal and serialize the tree in the list data
what you get is root followed by sets of children
it looks like
data = [root children children children .....]
consider the tree 
        0
      /   \
     1     2
    / \   / \
   3   4 5   6
when you serialize using level order traversal
data = [0 1 2 3 4 5 6]
data = [[root] [children of 0] [children of 1] [children of 2]]
for every node popped out of queue you just assign the next children set in data
that is why data_walker+1 and data_walker+2 might make this misleading
you are just assigning the next children set to the popped parent
better approach is 
i=0
assign left child
i+=1
assign right child
i+=1
an additional advantage of this style is that you don't have to check 
if i+1 and i+2 are in range, just do one check for i at the while loop and that
would be sufficient
"""

# When using level-order (BFS) serialization, what we're creating is essentially
#  a flattened representation of the tree by levels:
# [root, level1_node1, level1_node2, level2_node1, level2_node2, level2_node3, 
# level2_node4, ...]


# """ # During deserialization:
# # - Each popped parent from the queue is assigned the *next two unassigned values* 
# #   in the data list as children. 
# # - It’s NOT “children of parent at index X are at positions X+1 and X+2.”
# #   Instead, it’s: “for each parent popped, assign the next two values from data.”
