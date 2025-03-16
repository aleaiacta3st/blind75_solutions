class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while(low<high):
            mid = (low+high)//2
            if (nums[mid]>nums[high]):
                low = mid+1
            else:
                high = mid

        #this is finding the minimum in a rotated sorted array
        #at the end of finding minimum low=mid=high, let us see why.
        #the loop terminates when low catches up with high,
        #the search space has collapsed to a single element and that is what we have to return
        # the index of the minimum is the pivot
        # now all you have to do is just binary search the two sequences
        #index 0 to index pivot-1
        #index pivot to index len(nums)-1 
        
        pivot=low
        #take care to store the value of pivot because low keeps changing
        low = 0
        high = pivot-1
        mid = 0

        #Why exactly low = mid + 1 and high = mid - 1?
        #If nums[mid] is not the element you're looking for, 
        # you never want to check it again.
        #Hence, you exclude it explicitly:
        #   low = mid + 1 (ignoring mid, moving forward).
        #   high = mid - 1 (ignoring mid, moving backward).
        #What happens if you mistakenly write low = mid or high = mid?
        #Let's say you do low = mid mistakenly. Then in some scenarios, 
        # the search space won’t shrink:
        #low=5, high=6 → mid=(5+6)//2=5
        # wrongly do:
        #low = mid (again 5)
        #After next iteration, mid calculation gives the same value again.
        #You get stuck with low = mid indefinitely. Your array segment 
        # isn't shrinking, and the loop goes infinite.
        #Binary search works because every iteration reduces the range of 
        # elements you check by at least one.

        #binary search array from index 0 to index pivot-1

        while (low<=high):
            mid = (low+high)//2
            if(target<nums[mid]):
                high = mid-1 
            elif(target>nums[mid]):
                low=mid+1
            else:
                return mid
            
        #binary search array from index pivot to index len(nums)-1 
        low = pivot
        high = len(nums)-1
        mid = 0
        while (low<=high):
            mid = (low+high)//2
            if(target<nums[mid]):
                high = mid-1 
            elif(target>nums[mid]):
                low=mid+1
            else:
                return mid
        return -1
        