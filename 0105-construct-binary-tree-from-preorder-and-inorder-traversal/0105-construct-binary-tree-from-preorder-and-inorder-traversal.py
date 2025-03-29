# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        inorder_set={}
        for i in range(n):
            inorder_set[inorder[i]]=i
        index = [0]
        def dfs(left,right):
            if left>right:
                return None
            root = TreeNode(preorder[index[0]])
            root_index = inorder_set[preorder[index[0]]]
            index[0]+=1
            root.left = dfs(left,root_index-1)
            root.right = dfs(root_index+1,right) 
            return root
        return dfs(0,n-1)



# Use preorder to pick root. Use inorder to split left/right. 
# Recurse on slices. Stop when left > right.

# Preorder dictates the conquest order - 
# The first element in preorder is always the root of any subtree 
# you're building. Each position in preorder tells you exactly which '
# 'node to create next.
# Inorder reveals territory divisions - When you find a node's position '
# 'in inorder, everything to its left belongs to its left subtree, '
# 'everything to its right belongs to its right subtree.

# This works because these two traversals provide complementary information:

# Preorder gives you the sequence of creation (root → left → right)
# Inorder gives you the boundaries between subtrees (left → root → right)

# Together, they contain enough information to perfectly reconstruct the original tree structure. 

# With preorder alone, you cannot reconstruct the tree because:
# In preorder [Root, Left, Right], you know the root (first element), 
# but you cannot determine where the left subtree ends and right subtree begins.

# For example, with preorder [0,1,3,2,4,5]:

# We know 0 is root
# But is [1,3] the entire left subtree? Or just [1]? Or [1,3,2]?
# There's no definitive boundary

# The inorder traversal provides exactly this missing boundary information by 
# placing the root between its subtrees: [Left, Root, Right].
# With inorder [1,3,0,4,2,5]:

# When we find 0 at position 2
# Everything before (positions 0-1) must be in its left subtree [1,3]
# Everything after (positions 3-5) must be in its right subtree [4,2,5]




# the first element of preorder array is the root 
# find it in the inorder array 
# elements to the left form the left sub tree 
# right elements for the right subtree 
# preorder has the order in which nodes are visited 
# find the index of the node you are currently at 
    

# # Inorder Traversal Rule:
# # 1. Recursively traverse the left subtree
# # 2. Visit the root node
# # 3. Recursively traverse the right subtree
# # If a node is null/None, simply return without visiting
# # 
# #       0
#        / \
#       1   2
#      /   / \
#     3   4   5
#      \   \   
#       7   8     

# inorder traversal result would be: 3 -> 7 -> 1 -> 0 -> 4 -> 8 -> 2 -> 5

# Let me explain the concept of "recursively traversing a subtree" 
#     in more straightforward terms:
# Think of recursion as a self-repeating process - when you 
# "recursively traverse the left subtree," you're applying the same traversal '
# 'method to the left child node as if it were the root of its own smaller tree.
# Here's what it means practically:
# When you're at a node (let's call it the current node):

# For the left subtree: You go to the left child of your current node and 
# treat that left child as if it were the root of a brand new tree. 
# Then you apply the exact same traversal rules to this new "root."
# If this left child also has children, you keep going deeper, always following 
# the same pattern. You keep going left until you can't go left anymore.
# When you can't go left any further (you hit a null/None), you've reached the 
# end of that path and you start coming back up, visiting nodes or going right 
# according to the traversal type (inorder, preorder, or postorder).

# It's like a "nested" exploration - you fully explore one branch before moving '
# 'to the next one.'
# ''
# ''

# What dfs(left, right) does:
# “It builds and returns the root of the binary subtree 
# whose inorder elements lie between left and right, inclusive.”
# It:
# Picks the current root from preorder[index[0]]
# Finds that root’s position in inorder → say, mid
# Recursively builds:
# The left subtree from inorder[left ... mid-1]
# The right subtree from inorder[mid+1 ... right]
# Returns the fully constructed root node

# so left and right are indices of the inorder array

# Recursively building means:
# "Solve a small piece, then let the same function build the smaller parts."
# Like stacking blocks—place one, then call yourself to place the rest.
# That’s it. 
# Build part → call yourself → repeat till done.

# we first divide the inorder array at the root.the right subtree reaches 
# base case when root_index+1>right
# so the only case this hold true is when root_index = right
# That root had no right subtree.
# The inorder range to the right of it is empty, so recursion stops.


# we keep dividing intervals till we reach a stage where we know the answer.
# that is when that recursion call completes and gives back the answer to the recursion call 
# that called. connections are made bottom up. 

# when we run this program for constructing binary tree, there are many recursive 
# calls going out. does only one of them hit the base condition? 
# my question is, if the base condition is a target? how many of the many 
# recursive calls that call it are immeditaely next to it?

# No, not just one! Multiple recursive calls hit the base condition.
# The base condition (left > right) isn't a single destination - it's the edge 
# of the map, the boundary you reach in multiple places.

# very important
# Every leaf node in your final tree will trigger two base condition hits - 
# one when trying to build its left child and another when trying to build 
# its right child.
# Even internal nodes might trigger one base condition hit if 
# they have only one child.
# For a tree with N nodes, you'll have approximately N+1 '
# 'calls that hit the base condition.'
# 'For any leaf node in your tree:
# Both recursive calls from that node immediately hit the base condition
# These are the "immediate next" calls you're asking about
# For internal nodes with one child:
# One recursive call immediately hits the base condition
# The other builds a subtree





#                 #     0
#                 # 1         2
#                 #     3   4      5

# You can jump to dfs(k, k) by recognizing that a leaf node’s dfs 
# call has equal left and right bounds matching its inorder index, 
# without needing to trace the path from the top.
# The recursive call that creates the node with value 3 is dfs(k, k), 
# where k = inorder_set[3] is the index of 3 in the inorder list. 
# The subsequent recursive calls are:

# dfs(k, k - 1) for the left subtree, which returns None because k > k - 1.
# dfs(k + 1, k) for the right subtree, which returns None because k + 1 > k.
#     To jump into this call as a human:

# Identify 3 in the inorder list to get k.
# Recognize that since 3 is a leaf (no children, as subsequent calls 
# hit the base condition), the dfs call must 
# process a single-element range: dfs(k, k).
# This approach lets you pinpoint the exact x, y values (x = k, y = k) 
# responsible for creating node 3, satisfying your desire to focus on this small 
# part of the recursion without following the entire thread of execution. 
# You’ve effectively “jumped into the middle” by leveraging the node’s 
# properties and the algorithm’s structure!


# In the standard algorithm for constructing a binary tree from preorder and 
# inorder traversals, a recursive function—let’s call it dfs(left, right)—is 
# used to build the tree. This function operates on a range [left, right] of 
# indices in the inorder traversal:

# Preorder Traversal: Gives the root node first, followed by the left subtree, 
# then the right subtree.
# Inorder Traversal: Gives the left subtree, followed by the root, then the 
# right subtree.
 

# At each recursive call dfs(left, right), it selects the next unprocessed 
# element from the preorder list as the root of the current subtree. 
# Let’s denote this value as val, and its position in the preorder list is 
# tracked by a global index, say index[0].
# It then finds the position of val in the inorder list, 
# say at index k (where k is between left and right inclusive).
# The nodes before k in the inorder range [left, right] (i.e., [left, k-1]) 
# form the left subtree, and the nodes after k (i.e., [k+1, right]) 
# form the right subtree.
# The function creates a node with value val, recursively builds the 
# left subtree with dfs(left, k-1), and the right subtree with dfs(k+1, right).

# Each call to dfs(left, right) thus creates exactly one node—the root of the 
# subtree corresponding to the inorder range [left, right]—and then 
# delegates the construction of its left and right subtrees to further 
# recursive calls.    

# given the recursive call that builds parent P 
# (with inorder bounds left_P, right_P), the recursive calls 
# that will build its left and right children are:
# Left child → dfs(left_P, k_P - 1)
# Right child → dfs(k_P + 1, right_P)




        