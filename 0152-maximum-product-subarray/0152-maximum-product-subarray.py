class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod_so_far = nums[0]
        min_prod_so_far = nums[0]
        max_global=nums[0]

        #in max sum subarray, we discarded previous negative sum
        #but in product we cannot do that
        #as a negative product can multiply with a negative number in the future 
        #and become positive
        #what is min_prod_so_far tracking?
        # consider all subarrays ending at element i
        #someof them have negative products, some of them have positive products
        #that is what we are tracking
        #the ith element can start a new subarray if it does not combine with
        #the previous sequence or it can combine with the positive product
        #subarray or the negative product subarray
    
        for num in nums[1:]:
            k=max_prod_so_far
            max_prod_so_far = max(num, num*max_prod_so_far, num*min_prod_so_far)
            #max_prod_so_far is updated above. so store its value in k so
            #it can be used below
            min_prod_so_far = min(num, num*k, num*min_prod_so_far)

            max_global = max(max_global, max_prod_so_far)
            

        return max_global
        