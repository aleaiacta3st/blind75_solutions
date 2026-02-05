class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])

        visited=set()

        max_area=0


        def dfs(r,c):
            area=1
            visited.add((r,c))

            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr,nc = r+dr,c+dc

                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and grid[nr][nc]==1:
                    area=area+dfs(nr,nc)

            return area 



        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c]==1:
                    max_area=max(max_area,dfs(r,c))

        return max_area
        