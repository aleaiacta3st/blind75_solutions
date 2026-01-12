class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        twoSum={}
        for i in range(n):
            complement = target-nums[i]
            if complement in twoSum:
                return (i,twoSum[complement])
            else:
                twoSum[nums[i]] = i

        