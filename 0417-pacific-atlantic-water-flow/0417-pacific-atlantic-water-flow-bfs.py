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
        
        
        
        
        
 
