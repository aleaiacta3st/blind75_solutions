class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()

        adj_dict={}


        for i in range(n):
            adj_dict[i] = []


        for node,neighbor in edges:
            adj_dict[node].append(neighbor)
            adj_dict[neighbor].append(node)


        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor_nodes in adj_dict[node]:
                dfs(neighbor_nodes)

        count=0

        for node in adj_dict:
            if node not in visited:
                count=count+1
                dfs(node)

        return count
        