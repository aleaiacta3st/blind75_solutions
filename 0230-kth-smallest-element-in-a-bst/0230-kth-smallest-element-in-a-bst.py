# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [0]  # Using a list to make the counter mutable
    
        def inorder(node):
            if not node:
                return None
            
            # Traverse left subtree first
            left_result = inorder(node.left)
            if left_result is not None:
                return left_result
            
            # Process current node (count it)
            counter[0] += 1
            if counter[0] == k:
                return node.val
            
            # Traverse right subtree
            return inorder(node.right)  # Simply return whatever comes back
        
        return inorder(root)



# Yes, in-order is usually harder than pre-order for beginners. Here's why:
# 1. Traversal order
# Pre-order: Root → Left → Right
# In-order: Left → Root → Right
# Pre-order starts with the root—simple and intuitive. 
# You process the current node first, then recurse. Easy to trace.
# In-order requires holding off on processing the root until after traversing the
# left. This delayed action feels unnatural at first.

# 2. Mental model
# In pre-order, you’re doing something at each node before diving deeper.
# In in-order, you have to defer the action, which forces you to manage state 
# (in recursion or stack) more carefully.

# What is "delayed processing"?
# It means: You don’t act on a node the moment you reach it.
# Instead, you go left first, and only after that finishes, 
# you process the current node.

# 1. Dive all the way left (left subtree)
# 2. THEN process the current node (delayed)
# 3. THEN go right (right subtree)

# General Pattern (Recursive)
# def inorder(node):
#     if not node:
#         return
#     inorder(node.left)       # Step 1: go left
#     process(node)            # Step 2: process current node (delayed)
#     inorder(node.right)      # Step 3: go right
# You can swap out process(node) for any logic—validation, counting, 
# collecting values, etc.
# \U0001f4a1 node is the root of the current subtree.


# What is the brain trick?
# Wrong mindset:
# “I’m at a node. Let me do something.”
# Correct mindset:
# “Ignore the node. Go left. Once I can’t go left anymore, then I’ll start 
# processing nodes one by one on the way back.”
# You’re “postponing” action until the leftmost node is fully explored.


# Summary of Tips
# Burn the pattern: inorder(left) → process → inorder(right)
# Understand why: BST + in-order = sorted order. That’s the key.
# Don’t think in terms of “now”. Think in terms of when you’re allowed to act.
# Trace by hand a few traversals with a call stack. It will click.
# Use counters or flags when solving problems like Kth Smallest or BST validation.
# Avoid shortcuts—master recursive in-order before trying iterative.

# In-order traversal step-by-step:
# At a node, go left as far as possible.
# Once there’s no more left, process that node.
# Then backtrack one level up and process that node.
# After processing a node, go to its right child and repeat steps 1–3.

#         5
#        / \
#       3   7
#      / \
#     2   4
#    /
#   1
# Correct In-order Traversal: Left → Node → Right
# Let’s walk it step by step:
# Start at 5, go left to 3
# At 3, go left to 2
# At 2, go left to 1
# 1 has no left → process 1
# Go back to 2 → process 2
# 2 has no right → return to 3
# Now process 3
# Then go right to 4 → 4 has no children → process 4
# Back to 5 → process 5
# Go right to 7 → 7 has no children → process 7

# i meant to ask when i say inorder(node.left), how are we moving to 
# the left child? what is causing the movement?
# The function argument node.left is the move.
# That’s it.
# You're not moving physically—you're passing a reference to a 
# new node (the left child) into a new function call.

# Behind the scenes:
# Every TreeNode has .left and .right pointers.
# node.left returns the left child (another TreeNode object).
# When you call inorder(node.left), you're saying:
# “Run the same code, but now with the left child as the current node.”
# Boom—you’ve "moved."

# \U0001f501 So: movement = argument passing
# def inorder(node):
#     ...
#     inorder(node.left)  # ← "move" to left child
# This isn’t magic—node.left is just a pointer. Passing it to a recursive function
# transfers focus to that child.

# The movement down the tree happens because you pass node.left into the next 
# function call.
# It’s a logical shift, not a physical one. But structurally, you’re diving 
# into the left subtree by handing the left child to a copy of the same logic.
# That’s the movement you’re feeling but not seeing.

# ✅ Post-order Traversal:
# def postorder(node):
#     if not node:
#         return
#     postorder(node.left)     # Left
#     postorder(node.right)    # Right
#     process(node)            # Node

# ✅ Pre-order Traversal
# def preorder(node):
#     if not node:
#         return
#     process(node)            # Node
#     preorder(node.left)      # Left
#     preorder(node.right)     # Right

# i have heard some people say trust the recursion. what do they mean by that? 
# Don't try to micromanage the whole tree. Just focus on what each call does, '
# 'and trust that recursion will handle the rest.'

# Why people don’t trust recursion:
# Feels like a black box
# You can’t “see” the stack frames
# You worry about who processes what and when
# You try to track the entire tree at once

# Instead of thinking:
# “I’m walking the whole tree!”
# Think:
# “I’m writing code that handles one node correctly, assuming left and 
# right are already handled.”
# That’s trusting recursion.
# def inorder(node):
#     if not node:
#         return
#     inorder(node.left)
#     process(node)
#     inorder(node.right)
# Just trust:
# inorder(node.left) will correctly handle the left subtree
# After that, you’re at the right point to process node
# Then inorder(node.right) will handle the right side

# You’re not responsible for how the left/right work. You just say:
# “If I handle my node correctly, and assume the rest does too, 
# the whole thing works.”

# Recursion lets you ignore the big picture.
# You delegate the rest of the tree to future function calls.
# You only handle now.

# Think like this:
# “I’m not solving the whole problem.
# I’m just saying: ‘If you give me a node, I’ll do the right thing 
# for it assuming left and right are taken care of.’”

        