from collections import deque
def numIslands(grid):
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


An alternate concise solution
def numIslands(grid):
    if not grid:
        return 0
        
    m, n = len(grid), len(grid[0])
    visited = set()
    
    def dfs(i, j):
        # Base case: out of bounds or water or already visited
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0" or (i, j) in visited:
            return
            
        visited.add((i, j))
        
        # Explore in all 4 directions
        dfs(i+1, j)  # down
        dfs(i-1, j)  # up
        dfs(i, j+1)  # right
        dfs(i, j-1)  # left
    
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and (i, j) not in visited:
                dfs(i, j)
                count += 1
                
    return count