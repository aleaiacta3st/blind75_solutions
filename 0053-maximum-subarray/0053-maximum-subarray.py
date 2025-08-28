class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        global_max = nums[0]
        current_sum=nums[0]

        for i in range(1,n):
            current_sum = max(nums[i], current_sum + nums[i])
            if current_sum>global_max:
                global_max=current_sum 

        return global_max
        