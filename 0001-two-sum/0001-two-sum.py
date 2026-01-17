class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        twosum={}

        for i in range(n):
            complement=target-nums[i]
            if complement in twosum:
                return(i,twosum[complement])
            else:
                twosum[nums[i]]=i

        
        