class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n=len(nums)
        target = sum(nums)//2 

        if sum(nums)%2!=0:
            return False

        dp=[False]*(target+1)

        dp[0] = True 


        for i in range(n):
            for j in range(target,nums[i]-1,-1):
                if dp[j] or dp[j-nums[i]]:
                    dp[j]=True


        return dp[target]
        