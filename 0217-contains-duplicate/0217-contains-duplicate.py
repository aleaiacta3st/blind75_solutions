class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate=set()
        n=len(nums)

        for i in range(n):
            if nums[i] in duplicate:
                return True
            else:
                duplicate.add(nums[i])

        return False
        