class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        can_reach_atlantic=set()
        can_reach_pacific=set()

        atlantic_queue=deque()
        for j in range(n):
            atlantic_queue.append((m-1,j))
        for i in range(m):
            atlantic_queue.append((i,n-1))

        pacific_queue=deque()
        for i in range(m):
            pacific_queue.append((i,0))
        for j in range(n):
            pacific_queue.append((0,j))

        while atlantic_queue:
            (i,j)=atlantic_queue.popleft()
            if (i,j) not in can_reach_atlantic:
                can_reach_atlantic.add((i,j))
                for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if (a,b) not in can_reach_atlantic:
                        if 0<=a<m and 0<=b<n and heights[a][b]>=heights[i][j]:
                            atlantic_queue.append((a,b))

        while pacific_queue:
            (i,j)=pacific_queue.popleft()
            if (i,j) not in can_reach_pacific:
                can_reach_pacific.add((i,j))
                for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if (a,b) not in can_reach_pacific:
                        if 0<=a<m and 0<=b<n and heights[a][b]>=heights[i][j]:
                            pacific_queue.append((a,b))

        intersection_set = can_reach_pacific & can_reach_atlantic
        return [list(i) for i in intersection_set]


# observe that the queue is initially loaded with all ocean bordering nodes. 
# in dfs+recursion we did dfs on every node. but that is not the case here. 
# we might think that a bfs queue should be first filled with one node. 
# then it is popped out then filled with its neighbors and so on. 
# so why did our initial queue contain all ocean bordering nodes?

# In DFS:
# You start from one border node and recursively go to all reachable places.
# You do this for every border node individually.
# Each DFS call from each border cell explores outward.
# In BFS (iterative):
# Instead of running BFS once for each border cell (which would repeat setup and cost time),
# You load the queue initially with all border cells at once — they all start as the “first layer” of exploration.
# Then BFS expands from all of them simultaneously, level by level.
# Why does this work?
# Every border cell is a “source” — you’re letting them all spread out simultaneously.
# Each pop from the queue is like a wave expanding outward.
# This ensures no duplication, and each node is only visited when it can be reached 
# from the ocean border.
# If you started with only one node:
# You’d be doing BFS from just that cell.
# Then you’d have to repeat that BFS from every single border cell again.
# The combined BFS starting from all border cells together saves time and 
# does exactly the same work in parallel.

#multi-source bfs
# Multi-source BFS is a strategy where instead of starting BFS from one single source node,
# you start from multiple sources at once — all loaded into the queue together.
# All these sources are placed in the queue at the beginning.
# BFS expands outward from all of them simultaneously, layer by layer.
# It’s like starting multiple fires around a forest and watching them all 
# spread until they meet.
# It avoids redundant searches.
# It lets you find the shortest distance from any of the multiple sources to a target.
# The search is perfectly balanced — all sources expand in parallel.
# Classic use cases:
# The Pacific Atlantic Water Flow problem (exactly what you’re doing!)
# Finding the minimum distance from multiple obstacles or fires to every cell in a grid.
# Spreading influence, infection, or signal from multiple initial locations
        
        
        
        
        
        
    # DFS solution starts from here    
    #     m,n=len(heights),len(heights[0])
    #     can_reach_atlantic=set()
    #     can_reach_pacific=set()
        
    #     def dfs_atlantic(i,j):
    #         if (i,j) not in can_reach_atlantic:
    #             can_reach_atlantic.add((i,j))
    #             for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
    #                 if 0<=a<m and 0<=b<n and heights[a][b]>=heights[i][j]:
    #                     dfs_atlantic(a,b)
        
    #     def dfs_pacific(i,j):
    #         if (i,j) not in can_reach_pacific:
    #             can_reach_pacific.add((i,j))
    #             for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
    #                 if 0<=a<m and 0<=b<n and heights[a][b]>=heights[i][j]:
    #                     dfs_pacific(a,b)

    #     for j in range(n):
    #         dfs_atlantic(m-1,j)

    #     for i in range(m):
    #         dfs_atlantic(i,n-1)

    #     for i in range(m):
    #         dfs_pacific(i,0)

    #     for j in range(n):
    #         dfs_pacific(0,j)

    #     intersection_set = can_reach_pacific & can_reach_atlantic

    #     final_list=[]

    #     for i in intersection_set:
    #         final_list.append(list(i))

    #     return final_list
    






# for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
#                 if 0<=a<m and 0<=b<n and heights[a][b]>=heights[i][j]:
#                     dfs(a,b)
# should you append (a,b) to visited immediately and 
# should you check if it has been visited previously?
# No. Once the recursive call dfs(a,b) is called,
# that would take care of adding/not adding to visited

# Difference between a set and a list:
# A set contains only unique immutable elements
# Tuples are immutable
# Lists are not 
# Sets have O(1) lookup and are efficient than lists
# So store the coordinates of the grid in tuple format 
# To add elements to a set the syntax is set_name.add(immutable_item)
# To create an empty set, empty_set=set()

# Start from the nodes bordering the oceans
# Treat each grid as a node 
# This is a connected graph
# If you deploy,dfs/bfs, all nodes can be reached from all nodes 
# But while visiting each node, we take care to add only those nodes which 
# make the flow of the water to the ocean bordering node possible
# So, choose only those nodes where height of that node>=height of ocean bordering node 
# This ensures flow of water in the direction of the ocean boredring node 

# Observe the unpacking syntax in the for loops

# A set has nodes which can reach the pacific 
# The other set has nodes which can reach the antarctic 
# Take the intersection of them 
# But this will be a set 
# Convert it into a list to get the desired answer
        