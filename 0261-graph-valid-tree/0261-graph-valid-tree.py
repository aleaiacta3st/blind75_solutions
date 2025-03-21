class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            u,v = edge 
            adj_list[u].append(v)
            adj_list[v].append(u) 
        
        visited=set()

        def dfs(i):
            if i not in visited:
                visited.add(i)
                for neighbor in adj_list[i]:
                    if neighbor not in visited:
                        dfs(neighbor)
        count=0
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count=count+1

        
        return (count==1 and len(edges)==n-1)

# A tree should have a single connected component
# and n-1 edges where n is the number of nodes

#if a single dfs traversal is able to visit all nodes
#it implies that the graph has exactly 1 connected compoenent

#Observation
#The visited set serves a dual purpose in undirected graphs:
# Preventing cycle traversal - Stops the algorithm from getting 
# caught in actual cycles (A → B → C → A)
# Preventing edge ping-pong - In an undirected graph, when you 
# create the adjacency list:
# adj_list[u].append(v)
# adj_list[v].append(u)
# You create bidirectional references. Without the visited set:
# You'd go from A → B (because B is A's neighbor)
# Then immediately back B → A (because A is B's neighbor)
# Result: infinite A → B → A → B loop
# Your visited set ensures that once you've processed node A and '
# 'move to node B, you won't 
# come back to A again during that same traversal, even though A 
# appears in B's adjacency list.
        