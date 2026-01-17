class Solution:
    def rob(self, nums: List[int]) -> int:

        n=len(nums)

        if n==1:
            return nums[0]


        def helprob(houses):
            prev2=0
            prev1=0
            m=len(houses)

            for i in range(m):
                curr=max(prev2+houses[i],prev1)
                prev2=prev1
                prev1=curr

            return prev1



        return max(helprob(nums[0:n-1]), helprob(nums[1:]))

            


        
        