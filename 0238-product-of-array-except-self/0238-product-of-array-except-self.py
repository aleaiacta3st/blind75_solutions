class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums) 
        result = [1]*n 

        # left_product is the product accumulator

        # observe that

        # left_product(current number) = left_product(previous number) * previous number


        #for the first element, its left product should be 1
        left_product = 1

        for i in range(n):

            result[i] = left_product
            #update left_product for the next i
            left_product = left_product*nums[i]




        right_product=1    

        for i in range(n-1,-1,-1):
            result[i] = result[i]*right_product
            right_product=right_product*nums[i]

        return result


        