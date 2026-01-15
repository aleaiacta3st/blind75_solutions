class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1

        dp=[0]*(n+1)

        dp[0]=1
        dp[1]=1

        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if n==1:
        #     return 1

        # prev2=1
        # prev1=1

        # for i in range(2,n+1):
        #     curr=prev2+prev1
        #     prev2=prev1
        #     prev1=curr

        # return prev1


        