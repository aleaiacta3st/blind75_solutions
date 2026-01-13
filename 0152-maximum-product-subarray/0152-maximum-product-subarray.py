class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_i=nums[0]
        min_i=nums[0]
        max_product=nums[0]
        n=len(nums)

        for i in range(1,n):
            candidates = (max_i*nums[i], min_i*nums[i], nums[i])
            max_i = max(candidates)
            min_i = min(candidates)
            max_product=max(max_product,max_i)

        return max_product
