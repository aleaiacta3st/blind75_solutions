class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m=len(grid)
        n=len(grid[0])
        count=0
        visited=set()

        def bfs(r,c):
            visited.add((r,c))
            queue=deque([(r,c)])

            while queue:
                r,c=queue.popleft()

                for dr,dc in [(0,-1),(0,1),(-1,0),(1,0)]:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and grid[nr][nc]=='1':
                        visited.add((nr,nc))
                        queue.append((nr,nc))


        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in visited:
                    count=count+1
                    bfs(i,j)


        return count

        