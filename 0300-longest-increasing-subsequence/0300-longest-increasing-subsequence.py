class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1 

        n=len(nums)

        dp=[-float('inf')]*(n)
        dp[0]=1

        for i in range(1,n):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
                if nums[i]<=nums[j]:
                    dp[i]=max(dp[i],1)

        return max(dp)




        
        