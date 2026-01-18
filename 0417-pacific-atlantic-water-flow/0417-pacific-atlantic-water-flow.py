class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return [] 

        m=len(heights)
        n=len(heights[0])

        reaches_pacific=set()
        reaches_atlantic=set()

        def dfs(r,c,reaches_ocean):
            reaches_ocean.add((r,c))

            for dr,dc in [(0,-1), (0,1), (-1,0), (1,0)]:
                nr,nc = r+dr, c+dc

                if 0<=nr<m and 0<=nc<n and (nr,nc) not in reaches_ocean and heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,reaches_ocean)


        for i in range(n):
            dfs(0,i,reaches_pacific)

        for i in range(m):
            dfs(i,0, reaches_pacific)

        for i in range(m):
            dfs(i,n-1, reaches_atlantic)

        for i in range(n):
            dfs(m-1,i, reaches_atlantic) 

        return list(reaches_pacific&reaches_atlantic)
        