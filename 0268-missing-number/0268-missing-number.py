class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        accumulator = len(nums)
        for index,value in enumerate(nums):
            accumulator = accumulator^index^value
        return accumulator
        