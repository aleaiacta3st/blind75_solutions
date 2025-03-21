class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
        def bfs(land_node):
            queue=deque([land_node])
            while queue:
                (i,j)=queue.popleft()
                if (i,j) not in visited:
                    visited.add((i,j))
                    neighbor_list=[(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
                    for (a,b) in neighbor_list:
                        if (a,b) not in visited:
                            if updated_grid[a][b]=="1":
                                queue.append((a,b))
        count=0
        for land_node in list_of_land_nodes:
            if land_node not in visited:
                bfs(land_node)
                count=count+1

        return count
        