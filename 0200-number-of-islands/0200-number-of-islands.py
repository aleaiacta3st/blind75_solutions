class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # m,n = len(grid),len(grid[0])
        # updated_grid = [[0]*(n+2) for _ in range(m+2)]
        # for i in range(0,m):
        #     for j in range(0,n):
        #         updated_grid[i+1][j+1] = grid[i][j]
        # list_of_land_nodes=set()
        # for i in range(0,m+2):
        #     for j in range(0,n+2):
        #         if updated_grid[i][j]=="1":
        #             list_of_land_nodes.add((i,j))
        # visited=set()
        # def bfs(land_node):
        #     queue=deque([land_node])
        #     while queue:
        #         (i,j)=queue.popleft()
        #         if (i,j) not in visited:
        #             visited.add((i,j))
        #             neighbor_list=[(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
        #             for (a,b) in neighbor_list:
        #                 if (a,b) not in visited:
        #                     if updated_grid[a][b]=="1":
        #                         queue.append((a,b))
        # count=0
        # for land_node in list_of_land_nodes:
        #     if land_node not in visited:
        #         bfs(land_node)
        #         count=count+1

        # return count

# Updated Grid Explanation:
# 
# Original grid (m x n):
# +---+---+---+---+
# | 1 | 0 | 1 | 0 |
# +---+---+---+---+
# | 1 | 1 | 0 | 0 |
# +---+---+---+---+
#
# After updating ((m+2) x (n+2)):
# +---+---+---+---+---+---+
# | 0 | 0 | 0 | 0 | 0 | 0 |
# +---+---+---+---+---+---+
# | 0 | 1 | 0 | 1 | 0 | 0 |
# +---+---+---+---+---+---+
# | 0 | 1 | 1 | 0 | 0 | 0 |
# +---+---+---+---+---+---+
# | 0 | 0 | 0 | 0 | 0 | 0 |
# +---+---+---+---+---+---+
#
# Why do this?
# ➡️ Add padding borders to avoid index errors.
# ➡️ Allows simple neighbor checks (top, bottom, left, right) 
# without out-of-bounds conditions.

# deque([land_node]) V deque(land node)
# Land node, as we know, is a tuple.
# (a,b)
# deque([(2,3)]) V deque((2,3))
# The deque constructor iterates through its argument 
# deque([(2,3)]) 
#     Is list iterable? Yes. 
#     This list has only one element.
#     When popped, the tuple pops out as (2,3) 
# deque((2,3))
#     Is tuple iterable? Yes. 
#     This tuple has 2 elements in it.
#     When popped, it pops out 2 first, then 3. 
#     This is not what we want. 
# This is how a deque with 3 elements in the queue looks 
#     deque([(0, 1), (2, 3), (4, 0)])
#     A list with 3 elements 
#     A list is iterable. The elements(tuples) are popped 
#     one after the other
# The deque constructor looks at the outer structure — 
#     the "outer cover" — and then iterates through that.
# If the outer cover is a list, it will iterate over the list elements.
# If the outer cover is a tuple, it will iterate over that tuple’s elements (breaking it into pieces).


# Make a list of land nodes from the upgraded grid 
# From each land node, conduct a bfs. 
# The graph is connected so every node is connected to every other node 
# But we need to track to which other '1' nodes the 
# current 1 node is connected to
# Because an island can be more than the size of a single grid 

# +---+---+---+---+---+
# | 0 | 0 | 0 | 0 | 0 |
# +---+---+---+---+---+
# | 0 | 1 | 1 | 1 | 0 |
# +---+---+---+---+---+
# | 0 | 1 | 1 | 0 | 0 |
# +---+---+---+---+---+
# | 0 | 0 | 0 | 0 | 0 |
# +---+---+---+---+---+
#
#if you start bfs from any 1 node with the condition that we need to traverse only 1 nodes
# then all the 1 nodes together form an island 

# Once you form an island, remove all of them from subsequent considerations.
# No different island can be formed using these 1 nodes. 
# If it were possble, the bfs search would have discovered it.

# while queue:
#             i,j=queue.popleft()
#             if (i,j) not in visited:
#                 visited.add((i,j))
#                 neighbor_list=[(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
#                 for a,b in neighbor_list:
#                     if (a,b) not in visited:
#                         if updated_grid[a][b]=="1":
#                             queue.append((a,b))
# if we are encountering i,j for the first time, we add it to visited. 
# but if we visiting one of its neighbors (a,b) for the first time we dont
# add it to visited immediately. why?
# when we mark a newly discovered node as visited, we would lose the 
# opportunity to process its neighbors. so we must add it to visited, 
# only when we pop it, because that is when we start checking its 
# neighbors


# while queue:
#             i,j=queue.popleft()
#             if (i,j) not in visited:
#                 visited.add((i,j))
#                 neighbor_list=[(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
#                 for a,b in neighbor_list:
#                     if (a,b) not in visited:
#                         if updated_grid[a][b]=="1":
#                             queue.append((a,b))
# VARIABLE SHADOWING: THE i,j vs a,b LESSON
# When you use the same variable names in nested scopes (like nested loops)
# , the inner variable shadows (overwrites) the outer one.
# i,j = queue.popleft()  # Original coordinates 
# for i,j in neighbor_list:  # PROBLEM: Overwrites original i,j values!
#     # Now you've lost your original coordinates
# Rule to Remember
# Use distinct variable names for different conceptual entities.
# In graph traversals:
# Use one set of variables (e.g., i,j) for your current position
# Use different variables (e.g., a,b) for neighbors you're examining
# This maintains the distinction between "where you are" and 
# "where you might go next"

# are these different 
# (i,j)=queue.popleft() 
# [i,j]=queue.popleft() 
# i,j=queue.popleft() 
# for (a,b) in neighbor_list 
# for [a,b] in neighbor_list 
# for a,b in neighbor_list 
# In Python, these three expressions are functionally identical for 
# unpacking values:
# (i,j) = queue.popleft()  # Tuple unpacking with parentheses
# [i,j] = queue.popleft()  # List unpacking with brackets
# i,j = queue.popleft()    # Clean unpacking without symbols
# They all extract two values from the returned item and assign 
# them to variables.
# Similarly in loops:
# for (a,b) in neighbor_list:  # Unpacking with parentheses
# for [a,b] in neighbor_list:  # Unpacking with brackets
# for a,b in neighbor_list:    # Clean unpacking
# Just be consistent 
# If you're storing coordinates as tuples in visited set, '
# 'you must check with tuples: if (a,b) not in visited:
# If you're storing as lists, you must check with lists: '
# 'if [a,b] not in visited:'
# These are the default stylistic choices in python. no parentheses, 
# no square brackets
# i,j=queue.popleft() 
# for a,b in neighbor_list 

#dfs solution starts below

        m,n = len(grid),len(grid[0])
        updated_grid = [[0]*(n+2) for _ in range(m+2)]
        for i in range(0,m):
            for j in range(0,n):
                updated_grid[i+1][j+1] = grid[i][j]
        list_of_land_nodes=set()
        for i in range(0,m+2):
            for j in range(0,n+2):
                if updated_grid[i][j]=="1":
                    list_of_land_nodes.add((i,j))
        visited=set()
        def dfs(land_node):
            i,j=land_node
            if land_node not in visited:
                visited.add(land_node)
                neighbor_list=[(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
                for a,b in neighbor_list:
                    if (a,b) not in visited:
                        if updated_grid[a][b]=="1":
                            dfs((a,b))

        count=0
        for land_node in list_of_land_nodes:
            if land_node not in visited:
                dfs(land_node)
                count=count+1

        return count
        