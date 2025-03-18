"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque


class Solution:

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]


# While q: is Python shorthand for:
# "While the queue q is not empty, keep looping."
#  In more detail:
    # q is a deque (a double-ended queue).
    # In Python, any container (like a list or deque) evaluates to:
    # False when it's empty
    # True when it has elements
    # So while q: keeps running until q is empty.

# if not node:
#     return node
# Think of it as if (not node)
# edge case handler
# In Python, if not node: evaluates to True when:
#     node is None
#     node is an empty container
#     node is zero or False

# why should a neighbor be enqueued only when it is not in cloned
# When you enqueue a node, it is with the purpose of exploring 
# all its connections in the future. If you have already discovered 
# a node, there is no need to schedule it again in the queue

# Consider what would happen in a cycle - if Node A connects to Node B, 
# and Node B connects to Node A:
# Without the check, you would enqueue B, then while processing B, enqueue A again, 
# then while processing A, enqueue B again... an endless cycle!
# With the check, once a node is in 'cloned', we know it will be fully explored, 
# so you need not schedule it again in the queue.

# for neighbor in n.neighbors:
#     if neighbor not in visited:
#         # Clone the neighbor and put in the visited, if not present already
#         visited[neighbor] = Node(neighbor.val, [])
#         # Add the newly encountered node to the queue.
#         queue.append(neighbor)
#     # Add the clone of the neighbor to the neighbors of the clone node "n".
#     visited[n].neighbors.append(visited[neighbor])

# observe that the starting node is fully processed in the first iteration of the 
# for loop
# it is cloned, its neighbors are cloned, and these cloned neighbors are added to 
# the neighbor list of the clone 
# In dfs with recursion, the starting node though created first, its neighbor list 
# was completed the last

# Take the given node n. Its clone is created. Its neighbor list is updated with the correct neighbor clones.
# later when one of these neighbor clones is being processed, it should be updated with its own neighbor clones among which n would be present. 
# so we see that connections are being made both sides. 

# We want to correctly handle cases like a-b-c-a where there is a cycle 
# Having connections both ways like described i snot the same as having a cycle

# if neighbor not in visited:
#     # Clone the neighbor and put in the visited, if not present already
#     visited[neighbor] = Node(neighbor.val, [])
#     # Add the newly encountered node to the queue.
#     queue.append(neighbor)

# see the above lines of code. when a neighbor is not cloned. The if condition holds true.
# It is cloned and enqueued. This neighbor to node n can be a neighbor to some other 
# node and will come up for processing again. BUt we shouldnt clone and enqueue it again. 
# It has already been enqueued when it was first discovered. Just add the clone to 
# the neighbor list of the node that is being corrently processed and move on.

# If this check is absent, we enqueue the same nodes over and over and it never ends.
# In DFS with recursion, you'll hit an infinite recursion that crashes with a '
# 'stack overflow. You keep calling deeper and deeper on the same cycle of nodes '
# 'until your program explodes.
        