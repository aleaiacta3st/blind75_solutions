class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        n=len(nums)
        max_length=0
        for num in nums_set:
            if num-1 not in nums_set:
                temp=num
                current_seq_length=1 #nums[i] itself
                while temp+1 in nums_set:
                    current_seq_length+=1
                    temp=temp+1
                if current_seq_length>max_length:
                    max_length=current_seq_length
        return max_length

# The key insight: for each number in your dataset, ask not "what comes next?" but rather "am I the beginning of a sequence?"
# Only numbers without a predecessor (n-1) can begin a sequence! From these starting points, you can measure how far the consecutive chain extends before breaking.
        