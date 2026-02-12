class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        n=len(nums)

        farthest=0

        for index,jump in enumerate(nums):
            if index>farthest:
                return False
            else:
                farthest=max(farthest,index+jump)

        return True
