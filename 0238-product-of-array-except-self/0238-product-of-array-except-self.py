class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums) 
        #will create a list with 1s as its elements
        result = [1] * n 

        #the first element has no product to its left 
        # hence we must set its left proudct to 1, so that 
        # its entire product evaluates to its right product

        # we need left product x right product

        left_product=1 
        #we now move from left to right till the element in focus
        for i in range(n):
            result[i] = left_product
            #observe that the above line, in the first iteration 
            # sets result[0]=1 which is what we need. The next 
            # element will now use left_product=first element 
            left_product *= nums[i]

        
        #we now move right to left till the element in focus
        #range syntax is start,stop,step
        #if step<0, it means we need to go back, decreases
        #so we start from greater i to smaller i, 
        # this happens only when we move from right to left
        right_product=1
        for i in range(n-1,-1,-1):
        #element with index(n-1) is the last element
        #stop -1, so that will not be included, 
        #    final value i takes would be=0
        #-1 step, the values that i takes are decreasing
            result[i] *= right_product 
            #observe the change above when compared to the left product.
            #result[i] already has the left product in it before 
            # multiplicatopn by the right_product
            right_product *= nums[i]

        return result 


        