class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m=len(grid)
        n=len(grid[0])


        visited = set()

        def dfs(r,c): 
            visited.add((r,c))

            for (dr,dc) in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr,nc = r+dr, c+dc

                if nr>=m or nc >=n or nr<0 or nc<0 or (nr,nc) in visited or grid[nr][nc]!='1':
                    continue
                else:
                    dfs(nr,nc)



        islands=0

        for r in range(0,m):
            for c in range(0,n):
                if grid[r][c]=='1' and (r,c) not in visited:
                    islands=islands+1
                    dfs(r,c)


        return islands

        