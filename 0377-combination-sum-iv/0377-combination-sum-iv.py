class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            for j in nums:
                if (j<=i):
                    dp[i]=dp[i]+dp[i-j] 
        return dp[target]

# Consider a target amount i.
# Now think about what the final step would be to reach the target.
# If your final step is 1, the stop before is i-1
# If your final step is 3, the stop before is i-3
# If 1 and 3 are the only denominations you have, then you can reach i via 1 or 3.
# There is no other way. 
# Let dp[i] be the number of ways target i can be reached 
# i can be reached through path 1 or path 3
# dp[i-1] is the number of ways i-1 can be reached 
# dp[i-3] is the number of ways i-3 can be reached 
# we have already concluded that i can be reached only through 1 or 3
# dp[i] = dp[i-1]+dp[i-3]
# Think of it like this
# Your final destination is Chicago
# Chicago can only be accessed through Dallas or Houston 
# Dallas can be accessed in 7 different ways 
# Houston can be accessed in 3 different ways
# Therefore, Chicago can be accessed in 10 different ways 
# You can also imagine a big greater than symbol with Chicago on the right. 
# On the left imagine a crows feet above and below. These are the 
#     number of ways Dallas or Houston can be accessed.

# dp[0]=0 
# The number ways to reach 0 is 1. 
# You are using 0 coins but there is a way. Just don't use any coins.
        