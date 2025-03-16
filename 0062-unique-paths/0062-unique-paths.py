class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[0]*(n) for _ in range(m)]
        for i in range(0,m):
            dp[i][0]=1
        for i in range(0,n):
            dp[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]

#the number of ways to reach a cell is the sum of ways to 
# reach the cell to its left and the cell above it.

#0 based indexing
#elements in first row and first column of dp need to set to 1
#they are cases where either number of rows=1 or number of columns=1
#in all such cases, the number of paths possible =1, just walk straight
#observe that dp[1,1] is not 1 because dp[1][1] is actually 
# representing a square of size 2x2

#if you had padded the actual grid with a row of zeros and a column of zeros
#then dp[1,1]=1 because in that dp[1][1] actually denotes a single block
#you need not initialise any other element of the dp
        