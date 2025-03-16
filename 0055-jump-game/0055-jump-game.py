class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True #already at the destination
        farthest=0 #tracks how far we can reach
        for i in range(0,n):
            if (i>farthest): #current position is unreachable
                return False # assume i=5, farthest =4. 
                            #You can't reach i=5, 
                            # you absolutely cannot reach the 
                            # end of the array.
            if nums[i]>=1:
                farthest = max(farthest,i + nums[i])
            if farthest>=n-1:
                return True
        return False


#A greedy approach is an algorithmic strategy where 
# you make the locally optimal choice at each step, 
# hoping it will lead to the 
# globally optimal solution. 
# Instead of considering all possibilities 
# (like dynamic programming does), 
# greedy algorithms make the 
# best immediate decision and move forward.

#Instead of calculating every possible jump combination, 
# you're simply tracking "what's the furthest position 
# I can reach so far?

# Why Greedy Instead of DP?
# This problem appears in DP sections because it can be 
# solved with DP, but it's actually more efficient 
# with a greedy approach:

# DP approach - O(n²) time complexity:
# For each position, consider all possible jumps
# Build a table of reachable positions


# Greedy approach - O(n) time complexity:
# Only track the furthest reachable position
# Make a single pass through the array
        