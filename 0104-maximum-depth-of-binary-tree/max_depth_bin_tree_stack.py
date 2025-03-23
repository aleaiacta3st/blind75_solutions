def maxDepth(node):
    if not node:
        return 0
    stack=[(node,1)]
    current_max=0
    while stack:
        curr_node,depth=stack.pop()
        current_max=max(current_max,depth)
        if (curr_node.right):
            stack.append((curr_node.right,depth+1))
        if (curr_node.left):
            stack.append((curr_node.left,depth+1 ))
    return current_max


# Why does this algorithm work?
# A binary tree’s maximum depth is the length of the longest path 
# from the root to any leaf.
# In recursive DFS, the call stack keeps track of the current node and 
# its depth. In iterative DFS, you build that same mechanism manually 
# using a stack.
# Each element in your stack is a (node, depth) pair — this is your 
# explicit record of where you are and how deep you are.
# By popping one node at a time, you process that node at that recorded 
# depth.
# If this node has children, you push them with depth + 1 — simulating 
# the downward move along the branch.
# As you go, each time you pop, you know exactly how deep that node is. 
# If it’s deeper than the current max, update it.
# In the end, once every node has been processed (stack is empty),
# your current_max holds the maximum depth encountered.


# What is the call stack? What does it store?
# The function calls are stacked in recursion 
# Every function call has its parameters and local variables
#     for example
#     dfs(A)
#         fufufufn 
#         dfs(B)
#         i=i+1 
#     In this example, dfs function is stacked first
#     Its parameter is A. That is also stored. 
#     dfs(B) is the point where a recursive call is started
#     when dfs(B) returns, i=i+1 is executed. So the location
#     from where the original function should pick up is also stored
#     in the call stack
#     any local state for that call (like current depth, 
#                                    or partial results)
# Mental model:
# The stack holds function calls.
# Each call knows what node it’s working on.
# So indirectly, it’s holding the "context for that node."


# DFS with recursion
# imagine the below to be a stack 
# dfs(3)
# dfs(2)
# dfs(1)
# Once 3 is fully processed, dfs(3) is popped.
# Control returns to dfs(2), continuing with node = 2

#     A
#    / \
#   B   C
#  / \
# D   E
# push dfs(A)
# push dfs(B)
# push dfs(D)
# D has no children
# Pop dfs(D) as it is fully processed. 
# control goes back to dfs(b)
# push dfs(E)
# Pop dfs(E) as it has no children 
# control goes back to dfs(b)
# dfs(B) is fully processed 
# return control to A 
# push dfs(C)
# pop dfs(C) as it has finished processing and 
# has no children 
# control goes back to dfs(A)
# dfs(A) is fully processed 
# pop dfs(A)
# A node is treated as visited when its function call starts dfs(A)
# even before its children are added to the stack
# order of traversal is ABDEC


# DFS with own stack:
# start with stack =[A]
# pop it - in iterative approach, when a node is popped that is when we treat
# it as visited, not when it is pushed into the stack. this is a point of 
# difference between recursion approach and own stack approach 
# push right, left 
# B 
# C 
# pop B - B is visited when it is popped out of stack 
# add its children D and E (right left)
# D
# E
# C 
# pop D - D is visited when it is popped out of stack 
# E 
# C 
# pop E - E is visited when it is popped out of stack
# C 
# pop C - C is visited when it is popped out of stack

# The order of traversal is still ABDEC

# he Key Difference:
# Recursion: The call stack invisibly manages pushes/pops.

# Manual stack: You control pushes and pops, but the order in which 
# you push children (right first, then left) ensures the same DFS 
# exploration.

    
# Recursion with call stack 
# You visit a node the moment you make the recursive call on it 
# In other words, when you 'push' into the call stack — that’s the visit.

# dfs with own stack 
# You visit a node the moment you pop it from the stack.
# Why? Because at popping, you're holding the node in hand and '
# 'deciding what to do.
# Why not mark visited at push time?
# If you mark a node as visited when you push it into the stack, 
# you’re saying:
# "I’ve already dealt with this."
# But that’s not true yet!
# The node is merely waiting in line, not yet processed.
# It’s only sitting on the stack, waiting its turn.

# Processing = at pop time
# When you pop the node from the stack, it’s now your turn to:
# Read its value
# Update counters or max depth
# Print it, sum it, or record it
# Push its children for further exploration
# Only at pop time do you actually "process" the node.
# Before that, it’s just waiting in the queue (or stack) — 
# not done, not visited, just enlisted.

# Method	        Visit happens when	            Traversal order is order of:
# Recursive DFS	When the function call is made	Function call order
# Iterative DFS	When the node is popped	        Pop order from the stack

# Traversal order changes if you push right before left or 
# left before right.

# in dfs with recursion, it is the function calls that are stacked. 
# but in dfs with iteration and the stack that we made, 
# the actual nodes are getting stacked.

# Recursive DFS:
# The system call stack holds function calls, each with:
# The node itself
# The current state of that call (where it paused: before left, 
#                                 before right, etc.)
# The recursive function call stack invisibly manages both the node 
# and its context.
# You never see this structure. It’s automatic, elegant — but hidden.

# terative DFS (manual stack):
# You build that structure yourself.
# Instead of stacking function calls, you stack the actual nodes 
# // ===== IMPORTANT =====) 
# (and any context you need, like depth).
# You control exactly when something is processed, popped, or pushed.

# In other words, when you 'push' into the call stack — 
# that’s the visit.(dfs with recursion)
# then how is this true? do we process it as soon as we push it
# When you make a function call, you're effectively ‘pushing’ that '
# 'call frame onto the system call stack.
# But — here’s the key —
# The very first line after you enter that function call is usually:
# def dfs(node):
#     if not node:
#         return
#     process(node)  # <-- visit happens 
#     *immediately* upon entering the call
# The moment the function call begins (which is effectively the push), 
# you immediately process that node.
# You don’t "wait."
# It’s handled right there in that call frame before going deeper.


# deque creates a list.
# stack is already a list.
# that is why the difference at initialising.
# This distinction explains 
# why is deque([starting_node]) correct and not deque(starting_node)
# why is stack=[(root,0)] correct and not stack=[[(root,0)]]


