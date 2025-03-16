class Solution:
    def findMin(self, nums: List[int]) -> int:
        #after rotation, there are two ascending sequences
        #imagine a mountain
        #first sequence ascends
        #then a big drop from the peak at the minimum
        #then the second sequence starts ascending from the minimum
        #there are only two possibilities in the universe
        #nums[mid] and nums[high] are on the same side of the peak
        #nums[mid] and nums[high] are not on opposite sides of the peak
        #think and you will realise that such definite relation cannot be
        #deduced between nums[mid] and nums[low]
        #use these facts and frame your if statements
        #update low and high accordingly
        #we do low=mid+1, because we already know nums[mid]>nums[high]
        #so nums[mid] is not the minimum
        #hence mid need not be checked again. move to mid+1 index
        #on the other hand, we do high=mid because mid might
        #actually be the min element and we cannot exclude it
        #why low<high and not low<=high?
        #when the algo ends low=high=mid
        #so low<=high is always true and the loop never terminates
        #we want it to terminate when low = high, hence our condition is
        #while(low<high)
        #in classic binary search we want the loop to run even when a single element 
        #exists, so we can check if it is equal to the target, hence we need to account
        #for even low=high and hence condition is while(low<=high)
        low = 0
        high = len(nums)-1
        while(low<high):
            mid = (low+high)//2
            if (nums[mid]>nums[high]):
                low = mid+1
            else:
                    high = mid
        return nums[low]