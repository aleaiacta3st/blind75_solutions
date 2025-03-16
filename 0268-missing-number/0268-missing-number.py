class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #xor is associative as well as commutative
        #1 xor 2 xor 3 = 2 xor 1 xor 3
        #0 xor a = a
        #a xor a = 0
        #the values can be seen at two places
        # at the indices and as elements of the array
        # when we xor them both, duplicates get cancelled out
        # the missing number remains as it is present in the indices
        #but missing in the array elements
        n=len(nums)
        #the total number of elements should actually be n+1
        #but one is missing. it could be any of the indices
        #including the last index.
        # what would be the last index in an array of length n+1
        #where no element is missing? it should be n.
        #therefore the index should iterate from 1 to n
        #that is what we did below(important)
        #for the values themselves, it is an array of length n
        #so i should finally take a value of n-1
        indices_xor = 0
        for i in range(0,n+1):
            indices_xor = (indices_xor)^i 
        
        values_xor = 0
        for m in range(0,n):
            values_xor = (values_xor)^nums[m]
        
        return indices_xor^values_xor

        