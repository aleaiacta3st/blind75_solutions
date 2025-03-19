"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        cloned={}
        stack=[]
        stack.append(node)
        cloned[node]=Node(node.val,[])
        while stack:
            current=stack.pop()
            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor]=Node(neighbor.val,[])
                    stack.append(neighbor)
                cloned[current].neighbors.append(cloned[neighbor])
        return cloned[node]

# this solution looks very similar to bfs solution. 
# in dfs with recursion, i could very easily see that we are doing a dfs, 
# reaching a neighbor node, then going to its first neigh bor, then going 
# to its first neighbor etc. 
# but dfs+iteration looks like i am doing a bfs again.

# The key difference lies in the data structure used:
# # BFS uses a queue (FIFO)
# current = queue.popleft()  # Process nodes in order they were discovered
# # DFS uses a stack (LIFO)
# current = stack.pop()  # Process most recently discovered node first
# This seemingly small difference creates entirely different traversal 
# patterns:
#     1
#    / \
#   2   3
#  / \
# 4   5

# BFS traversal: 1, 2, 3, 4, 5 (level by level)
# DFS traversal: 1, 3, 2, 5, 4 (assuming neighbors are processed left to right)

# The recursive DFS "feels" more like depth-first because the 
# call stack naturally creates the deep-diving behavior. 
# With iterative DFS, you have to explicitly manage that 
# behavior with a stack.
# Both implementations are valid DFS approaches - they just express 
# the algorithm differently. The stack version is usually preferred 
# for very deep graphs where recursive calls might cause stack overflow.

# when a program becomes a process, it has both heap and stack. This stack 
# where functions are placed one above the other, is in the stack area. 
# when you create a stack explicitly, is it on the heap.
# When a program becomes a process, its memory is divided into segments:
#     The text/code segment (program instructions)
#     Data segment (global/static variables)
#     Stack (function call frames)
#     Heap (dynamically allocated memory)
# The call stack in the dfs+recursion method is in the stack area of the 
# process memory. It's automatically managed by the system and has a fixed'
# ' size limit. This is why very deep recursion can cause "stack overflow" errors.'
# When we explicitly create a stack in our code:
# stack = []  
# now we are creating a data structure that lives on the heap, 
# not the stack area. The heap is for dynamically allocated memory and is 
# typically much larger than the stack.
# This is why iterative DFS can handle much deeper graphs than recursive 
# DFS - your explicit stack on the heap can grow much larger than the call 
# stack is allowed to.

        
