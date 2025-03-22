class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        updated_intervals=[]
        for start,end in intervals:
            if end<newInterval[0]:
                updated_intervals.append([start,end])
            if end>=newInterval[0] and start<=newInterval[1]:
                start_merge = min(start,newInterval[0])
                end_merge = max(end,newInterval[1])
                newInterval=[start_merge,end_merge]
        updated_intervals.append(newInterval)
        for start,end in intervals:
            if start>newInterval[1]:
                updated_intervals.append([start,end])
        return updated_intervals


# The key insight is to keep updating the new interval
#don't immediately append to updated list after the first
# encounter between new interval and an original overlapping
# interval
# This is because this new interval might possibly overlap with
# other original intervals

# Alternate solution
# def insert(intervals, newInterval):
#     result = []
#     i = 0
#     n = len(intervals)
    
#     # Add all intervals ending before newInterval starts
#     while i < n and intervals[i][1] < newInterval[0]:
#         result.append(intervals[i])
#         i += 1
    
#     # Merge overlapping intervals
#     while i < n and intervals[i][0] <= newInterval[1]:
#         newInterval[0] = min(newInterval[0], intervals[i][0])
#         newInterval[1] = max(newInterval[1], intervals[i][1])
#         i += 1
    
#     # Add the merged interval
#     result.append(newInterval)
    
#     # Add remaining intervals
#     while i < n:
#         result.append(intervals[i])
#         i += 1
    
#     return result

# This makes use of the fact that the input is a list of lists
# so it mimics a 2d array and we can clearly lable each start and 
# end of an endpoint as list[start][end]
# Observe that i value is updated continuously
# It is never reset between loops

# This problem turned out to be relatively easier as the intervals
# were sorted in ascending order of start time.

        