class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        #if memo goes in the helper function, it is reset at every function call
        #nothing is stored

        # Returns the max subarray sum starting exactly at index i.
        def helper(i):
            if i in memo:
                return memo[i]
            # Base case: last element only
            if i == len(nums) - 1:
                memo[i] = nums[i]
            else:
                # Either take just nums[i], or extend with subarray starting at i+1
                memo[i] = max(nums[i], nums[i] + helper(i + 1))
                #this is where i have trouble understanding. i think of it like this. 
                #you are at index i. now element at index i can be included in the      #subarray or it could be excluded from the subarray.
                #if included subproblem(i) = element at i + subproblem(i+1)
                #if excluded subproblem(i) = subproblem(i+1)

                #If subproblem(i) = “best subarray starting exactly at i,” then you cannot skip i. Your choice is simply
                #subproblem(i)=max(nums[i],nums[i]+subproblem(i+1))
                #Either you take only nums[i], or you extend that subarray by adding the (possibly positive) best‐start at i+1.
            return memo[i]
    
        best = float('-inf')
        # Try every possible start index
        for i in range(len(nums)):
            best = max(best, helper(i))
        return best
        