# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# def maxDepth(root):
#     max_depth=0
#     depth=0
#     def dfs(node):
#         if not node:
#             max_depth=max(max_depth,depth)
#             return
#         for neighbor in [node.left,node.right]:
#             depth+=1
#             dfs(neighbor)
#     dfs(root)
#     return max_depth
# ⚠ Scope issue explanation:
# If a variable is defined outside a function (like depth = 0) 
# and we modify it (depth += 1) inside the function without declaring it global/nonlocal,
# Python treats it as a new local variable.
# But trying to read its value before it’s locally defined causes an UnboundLocalError.
# ✅ Solution: Pass depth as a parameter into recursive calls to maintain proper scope.

# ✅ If you only read a variable inside a function (no assignment),
# Python will use the variable from the outer scope without error.
# ❗ But if you assign to it inside the function, Python treats it as a local variable.
# Reading before assignment in that case causes UnboundLocalError.

# in graph problems, i was able to add elements to the visited set. 
# visited was declared an empty set outside the function. so how did that work?
# When you mutate a mutable object (like adding to a set or list) inside a function, it works.
# Why? 
# Because you're not reassigning the variable — you're modifying the object it points to.
# Example that works:
# visited = set()
# def dfs(node):
#     visited.add(node)  # ✅ This is allowed — you're modifying the set object
# Python allows this because visited is still pointing to the same set object, and 
# you're only calling methods on it.

# Example that fails:
# visited = set()
# def dfs(node):
#     visited = set()  # ❌ This reassigns visited to a new object locally — 
#     shadowing outer visited

# ✅ Mutating a mutable outer variable (like visited.add()) inside a function works fine.
# ❗ Reassigning the variable itself inside the function creates a local shadow variable, 
# causing scope issues.

# A local shadow variable is a new local variable with the same name as an outer variable.
# It hides ("shadows") the outer variable inside that function scope.
# The outer variable remains unchanged, but inside the function, only the local shadow 
# is used.

# Critical insight: return dfs(root) vs dfs(root)
# - dfs(root) alone: Executes the function but discards its return value
# - return dfs(root): Executes the function and passes its result back to the caller
#
# Without the 'return' keyword, your calculated result never makes it back to
# whoever called your function. The computation happens but the answer is lost.

# Binary Tree vs Graph Traversal Styles:
#
# Graph style (using loops):
#   for neighbor in [node.left, node.right]:
#       dfs(neighbor)
#
# Binary tree style (direct calls):
#   left_result = dfs(node.left)
#   right_result = dfs(node.right)
#   return 1 + max(left_result, right_result)
#
# The binary tree style is preferred for trees because:
# 1. It clearly shows we're working with a binary structure
# 2. It makes processing individual subtree results more explicit
# 3. It's more flexible when left/right subtrees need different handling
# 4. It's more natural for the recursive "bottom-up" calculation pattern
#    common in tree problems

# Keeping state requires a helper function so that state variables 
# (like counters or accumulators)
# can live outside the recursive calls but still be updated by them.
# Without state, recursion can just return values directly, no helper needed.

#         3
#        / \
#       9   20
#          /  \
#         15   7
# Recursive call stack breakdown:
# dfs(3)
    # Calls dfs(9)
        # Calls dfs(None) ➡️ returns 0
        # Calls dfs(None) ➡️ returns 0
        # Returns 1 + max(0,0) = 1 for node 9
    # Calls dfs(20)
        # Calls dfs(15)
            # Calls dfs(None) ➡️ 0
            # Calls dfs(None) ➡️ 0
            # Returns 1 + max(0,0) = 1 for node 15
        # Calls dfs(7)
            # Calls dfs(None) ➡️ 0
            # Calls dfs(None) ➡️ 0
            # Returns 1 + max(0,0) = 1 for node 7
        # Returns 1 + max(1,1) = 2 for node 20
    # Finally, dfs(3) returns 1 + max(1, 2) = 3


    # Mental Approach Checklist for Tree Recursion Problems
# 1. Clarify the question:
# What is being asked? Usually: "From each node, what is the result if 
# I go down to its children and combine their results?"
# 2. Identify if it's a tree (not a graph):
# No cycles, no visited set needed.
# Each node has at most two children (binary tree).
# 3. Think return-value first, not state:
# Instead of maintaining external state, aim to return a value from each call.
# Ask yourself: "What will I return to my parent that helps them compute their answer?"
# 4. Ask both children and combine answers:
# Typical pattern: return 1 + max(left_child_result, right_child_result)
# If a node is None, return 0.
# 5. Visualize a tiny example tree:
# Example:
#     1
#    / \
#   2   None
# dfs(2) returns 1
# dfs(None) returns 0
# dfs(1) returns 1 + max(1,0) = 2
# 6. Trust bottom-up recursion:
# Leaves return 1 (their depth), parents just take the max and add 1.
# No tracking, no global variables needed.
# 7. Confirm by mentally running through one level:
# For each node: "I ask my left and right children for their numbers, take the 
# bigger one, add one for myself, and return it."
# 8. Key mental mantra:
# In graphs: store and track. In trees: return and combine.
            