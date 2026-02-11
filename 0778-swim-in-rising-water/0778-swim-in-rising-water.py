class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        heap=[]
        heapq.heappush(heap,((grid[0][0],(0,0))))
        visited={(0,0)}

        r=len(grid)
        c=len(grid[0])

        while heap:
            tallest,cell=heapq.heappop(heap)
            row,col=cell
            if cell==(r-1,r-1):
                return tallest
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr,nc=row+dr,col+dc
                if 0<=nr<r and 0<=nc<r and (nr,nc) not in visited:
                    heapq.heappush(heap,((max(grid[nr][nc],tallest),(nr,nc))))
                    visited.add((nr,nc))



            
        