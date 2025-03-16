class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        container = {}  # Key: number, Value: index
        for i in range(len(nums)):
            complement = target - nums[i]  # What we need to find
            if complement in container:   # Already seen it?
                return [container[complement], i]  # Return indices
            container[nums[i]] = i  # Add current number to map
        return []  # No solution found   
        