class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n 
        if (n==0):
            return 0
        if (n==1):
            return nums[0]
        dp[0]=0 
        dp[1]=nums[1]
        for i in range(2,n):
            if (i==n-1):
                dp[i]=dp[i-2]+nums[i]
            else:
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        
        dq=[0]*n
        dq[0]=nums[0]
        dq[1]=max(nums[0],nums[1])
        for i in range(2,n):
            if (i==n-1):
                dq[i]=dq[i-1]
            else:
                dq[i]=max(dq[i-1],dq[i-2]+nums[i])

        return(max(dp[n-1],dq[n-1]))

# The circular nature only matters for the houses that form the "ends" of the circle. 
# For all other houses, the local decision-making is identical to the linear case.
# Consider this: if houses form a circle, houses[0] and houses[n-1] are neighbors. 
# Therefore, robber must decide:
#     Either rob houses[0] through houses[n-2], leaving the last house untouched
#     Or rob houses[1] through houses[n-1], leaving the first house untouched
#     This transforms one circular problem into two linear problems - 
#         each solvable using the technique you mastered in House Robber I. 
#         The ultimate prize is simply the greater bounty between these two heists. 
# 
# The only new relationship that House Robber II introduces (compared to House Robber I) is the 
# fact that house 0 and house n-1 are connected. That’s it.
# House 2 and House n-1 are NOT directly connected—there is still a valid DP chain.
# The reason the first and last house are special is that stealing from both is forbidden.
# That means:
# The recurrence relation still holds for all other houses as if it were linear.
# When you split the problem into two linear cases, each one is fully valid as a House Robber I case. 


        