class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        
        return result




















        # intervals.sort()
        # n=len(intervals)
        # final_list=[intervals[0]]
        # for i in range(1,n):
        #     if intervals[i][0]<=final_list[-1][1]:
        #         final_list[-1][1]=max(intervals[i][1],final_list[-1][1])
        #     else:
        #         final_list.append([intervals[i][0], intervals[i][1]])
        # return final_list



# for loop, i can only jump by 1 for every loop 
# if you sense the pointer needs to update more than once per loop, then don't use for

# Algorithm explanation:
# 1. Sort intervals by start time to ensure we process them in order
# 2. Initialize result list with the first interval
# 3. For each remaining interval:
#    a. If it overlaps with the last interval in our result:
#       - Merge by extending the end time to the maximum of both intervals
#    b. If no overlap:
#       - Add the new interval to our result unchanged
# 4. Return the merged intervals list
#
# Key insight: Sorting by start time guarantees we only need to compare each interval
# with the last interval in our result. After sorting, any potential overlaps must 
# involve adjacent intervals in the sorted order. This transforms a potentially complex
# problem into a simple linear scan.
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for storing the result
#
# Example: [[1,3], [2,6], [8,10], [15,18]]
# Sort: Already sorted by start time
# Initialize: final_list = [[1,3]]
# i=1: [2,6] overlaps with [1,3] → update to [1,6]
# i=2: [8,10] doesn't overlap with [1,6] → add to result
# i=3: [15,18] doesn't overlap with [8,10] → add to result
# Final result: [[1,6], [8,10], [15,18]]
        