class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            u,v=edge 
            adj_list[u].append(v)
            adj_list[v].append(u)
        adj_list_dict={}
        for k in range(n):
            adj_list_dict[k] = adj_list[k]

        visited=set()

        def dfs(i):
            if i not in visited:
                visited.add(i)
                for neighbor in adj_list[i]:
                    if neighbor not in visited:
                        dfs(neighbor)

        no_of_connected_components=0

        for i in range(n):
            if i not in visited:
                dfs(i)
                no_of_connected_components+=1

        return no_of_connected_components

# every time you encounter a node not yet visited, 
# that’s the start of a new connected component.

#create an adjacency list from the given edges array
#start dfs
#A dfs at a node will traverse all the nodes connected to it
#to prevent getting stuck due to cycles, use a visited set

# Visual Example of Multiple Components:
#
#    0 — 1 — 2        (Component 1)
#
#    3 — 4            (Component 2)
#
#    5                (Component 3, isolated node)
#
# Start DFS from 0: visits (0,1,2) — component count = 1
# Next unvisited: node 3 — visits (3,4) — component count = 2
# Next unvisited: node 5 — visits (5) — component count = 3
        