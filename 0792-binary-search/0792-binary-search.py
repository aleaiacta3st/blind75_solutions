class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lo=0
        hi=n-1
        while lo<=hi:
            mid=(lo+hi)//2
            if target<nums[mid]:
                hi=mid-1 
            elif target>nums[mid]:
                lo=mid+1 
            elif target==nums[mid]:
                return mid 
        return -1
        




# / - true division returns a float 4.0 5.1 
# // - floor division - rounds down
# everytime you divide the range should go down 

# Bin search, systematically reduces the search space to a single element.

# If you use left<right, it will not check the lone element standing with left=right. So you would need an additional check. 

# So use while left<=right, this will check the final lone number too.

# why are the +1 and -1 important, when the search space reduces to 2, the next iteration should make the search space into size 1.
# without +1 or -1, observe that search space will not reduce. it will stay at 2. you are stuck in an infinite loop. 

# one mre reason, you already cecked if target<nums[mid] or >nums[mid]. so our answer is definitely not index mid. so remove that from future considerations.
        