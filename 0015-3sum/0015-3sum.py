class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #2 pointer approach
        #fix an anchor and start moving the two pointers
        #calculate the sum of the two pointers
        #depending on their sum, comparing it with anchor, 
        # frame the if conditions
        nums.sort()
        # sort the array
        answer=[]

        for i in range(len(nums)-2):
            #to get a triplet, as we increase i, we must have atleast 
            # two elements after i, the range makes sure of that. if we 
            # do not fix it properly, inside the while loop nums[left] or 
            # nums[right] may go out of bounds

            #we skip duplicates at two places
            #outerloop- eliminate same anchor with if loop
            #innerloop - eleiminate same pairs with while loop

            if (i>0 and nums[i]==nums[i-1]):
                continue
            # contnue ends the current iteration and goes to the for loop again
            # this step is to eliminate the duplicates at the anchor i
            #first step i=0, so i=0 goes thru
            # for the second iteration i>0 and we need to check the if condition
            # if it is the same as the previous element, we skip it
            #Essentially, you’re saying, “If this number is the same as the last one, 
            # I’ve already searched all pairs for that same starting value.”
            left=i+1
            right = len(nums)-1
            while (left<right):
                if (nums[left] + nums[right] > -nums[i]):
                    right=right-1
                    #sum of pair is higher. so we need to decrease it.
                    #array is sorted. so bring the right pointer to the 
                    # left towards lesser values to decrease the sum
                elif (nums[left] + nums[right] < -nums[i]):
                    left=left+1
                    #sum of pair is lower. so we need to increase it.
                    #array is sorted. so bring the left pointer to the 
                    # right towards greater values to increase the sum
                else :#triplet found, record values
                    answer.append([nums[i], nums[left], nums[right]])
                    #now both pointers need to move
                    #if they do not move, the next iteration of while loop
                    #again enters the else block, will detect the same triplets
                    #stuck in a loop
                    left+=1
                    right-=1
                    #now avoid the same duplicate pairs for a given anchor
                    #why is the left<right condition important
                    #the left and right are updated manually in the if elif else block
                    # we arent checking if they are out of index
                    #the check happens only after we break out of ifelif
                    #but below we are trying to access nums[left] and nums[right]
                    #so we need an additional check to make sure they are not out of bounds
                    #left is increasing, right is decreasing
                    #by checking left<right,
                    #we impose a lower bound of left on right
                    #we impose a higher bound of right on left
                    while (left<right) and (nums[left]==nums[left-1]):
                        left+=1
                    while (left<right) and (nums[right]==nums[right+1]):
                        right-=1

        return answer
        