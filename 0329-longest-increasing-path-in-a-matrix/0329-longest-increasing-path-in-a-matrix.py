class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m=len(matrix)
        n=len(matrix[0])

        memo={}


        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            result=0
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>matrix[r][c]:
                    result=max(result,dfs(nr,nc))
            memo[(r,c)]=1+result
            return memo[(r,c)]



        max_length=0

        for r in range(m):
            for c in range(n):
                max_length=max(max_length,dfs(r,c))


        return max_length



        