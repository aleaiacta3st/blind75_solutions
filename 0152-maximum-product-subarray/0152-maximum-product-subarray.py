class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxprod=nums[0]
        minprod=nums[0]
        global_max=nums[0]

        for i in range(1,n):
            candidates=(maxprod*nums[i],minprod*nums[i],nums[i])
            maxprod=max(candidates)
            minprod=min(candidates)
            global_max=max(maxprod,global_max)

        return global_max
        