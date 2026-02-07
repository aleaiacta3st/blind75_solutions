class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])


        queue=deque()
        fresh=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh=fresh+1
                

        minutes=0

        while queue and fresh>0:
            k =len(queue)
            for i in range(k):
                r,c=queue.popleft()
                for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nr,nc=r+dr,c+dc 
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh=fresh-1
                        queue.append((nr,nc))
            minutes=minutes+1 


        return -1 if fresh>0 else minutes

