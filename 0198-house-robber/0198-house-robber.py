class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp=[0]*(n)
        dp[0] = nums[0]
        dp[1]=max(nums[0], nums[1])
        for i in range(2,n):
            dp[i]= max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]

# dp[i] is the max amount of booty possible till house i
# You are at the ith house and deciding if you should hit it
# If you choose to hit it
#   then your current booty is value from that house 
#   + 
#   booty accumulated till house i-2
# i-1 is out of contention as it is adjacent to i and we have decided to hit i
#if we choose not to hit i,
#   it means we have hit i-1, therefore 
#   booty at house i = booty accumulated till house i-1
# choose the maximum of the 2. that is our recurrence relation
# 
#There might be some confusion as indices of the dp array and nums array may not match
# if we assign a cell for a scenario where there are no houses in the dp array
#dp[0]=0 and dp[1]-indicates a scenario where there is just one house on the street
#observe that index of the house in the dp table is 1 but in the nums array it is at index 0
# so that is a source of confusion
#to avoid it, i have made lengths of the dp array and nums the same
#i have directly calculated values for dp[0] and dp[1] and made the for loop start from 2
        