class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_ending_i=nums[0]
        global_best=nums[0]
        n=len(nums)

        for i in range(1,n):
            best_ending_i = max(best_ending_i+nums[i], nums[i])
            global_best = max(global_best, best_ending_i)

        return global_best


        