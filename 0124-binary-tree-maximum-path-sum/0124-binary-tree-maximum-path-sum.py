# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = [float('-inf')] 
        def dfs(root):
            if not root:
                return 0 
            left_gain = dfs(root.left)
            left_gain = max(0,left_gain)
            right_gain = dfs(root.right)
            right_gain=max(0,right_gain)
            max_path_sum[0]=max(max_path_sum[0], root.val+left_gain+right_gain)
            return (root.val+max(left_gain,right_gain))
        dfs(root)
        return max_path_sum[0]


# The solution uses a depth-first search (DFS) with a clever trick: 
# a single variable max_path_sum (a list so it’s mutable across recursive calls) 
# tracks the global maximum path sum, while dfs returns a different value used for recursion
# instead of this list trick, inside the helper dfs function, we can just do nonlocal max_path_sum
# that would also work.

# The “inverted V” is a superset: it accounts for:
# Downward lines (if one side is zero or negative)
# Single nodes
# Proper inverted forks
# That’s why you don’t need a separate comparison for purely downward paths.
# They’re already considered at every node as part of the V calculation.

# For every node, calculate two values.
# In both cases, the node is included in the path.
# 1. The node may be part of an inverted V shaped path which reaches its max height 
# at this node and descends
# max sum = node value + left gain + right gain 
# 2. The node is part of a path that is coming down from its parent
# max sum = node value + max(left gain, right gain)
# This is because A path must be a single, continuous sequence without branches, and 
# forking at a node creates a structure with three connections (one in, two out), 
# which isn’t a valid path by definition. The algorithm enforces this by ensuring that 
# paths extend along a single route, maintaining the problem’s constraints while still 
# finding the maximum possible sum.

# we compare the inverted structure immediately with the global maximum and update it 
# The max downward sum, we return, for use by the parent of the current node.

# the dfs function returns the maximum downward sum of a node 
# as a side effect, it also updated the global maximum 

# This problem is different as we calculate two different values in every recursive call,
# but we only return one value to the parent recursive call.

# Space complexity 
# worst case O(n)
# Best case O(log n)
#             1
#          /     \
#        2         3
#       / \       / \
#      4   5     6   7
# What does the stack look like as you do dfs(root)?
# Call dfs(1) → stack: [1]
# Go left: call dfs(2) → stack: [1, 2]
# Go left: call dfs(4) → stack: [1, 2, 4]
# No children → return and pop → back to stack: [1, 2]
# Go right: call dfs(5) → stack: [1, 2, 5]
# No children → pop to: [1, 2]
# Done with node 2, pop back: [1]
# Go right: call dfs(3) → stack: [1, 3]
# Continue similarly.
# \U0001f449 Maximum call stack depth?
# At most 3 calls active (root → child → grandchild).
# Height = 3 levels.

#     1
#      \
#       2
#        \
#         3
#          \
#           4
# Call dfs(1) → [1]
# Call dfs(2) → [1, 2]
# Call dfs(3) → [1, 2, 3]
# Call dfs(4) → [1, 2, 3, 4]
# Return, pop.
# \U0001f449 Maximum call stack depth?
# 4 calls active at one point.
# Stack depth = height = number of nodes = N.
        