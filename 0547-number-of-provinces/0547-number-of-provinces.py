class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited=set()

        n=len(isConnected)

        def dfs(node):
            visited.add(node)
            for neighbor in range(n):
                if neighbor not in visited and isConnected[node][neighbor] == 1:
                    visited.add(neighbor)
                    dfs(neighbor)

        provinces=0

        for node in range(n):
            if node not in visited:
                provinces=provinces+1
                dfs(node)

        return provinces

        