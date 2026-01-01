class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # sort by END
        count = 1
        last_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= last_end:
                count += 1
                last_end = intervals[i][1]
        
        return len(intervals) - count




# we are making a list without intervals overlapping so i know that the final is a list which contains non overlapping intervals. difference between this list and the original list will tell me how many intervals we removed to make the given list into an non overlapping interval list. but how do i know that i have removed the minimum number of intervals to achieve this conversion.

# Real-world Analogy
# Think of it like conference room scheduling:

# If you always select the meeting that ends earliest, you leave more time for future meetings
# Any other strategy would either give the same result or require more removals

# The mathematical guarantee comes from this property: by always choosing the earliest-ending interval, we maximize our options for including future intervals, which naturally leads to the minimum number of removals.
    
# Keep earliest-ending intervals when possible: This maximizes our options for the future. what does this mean
# The statement "Keep earliest-ending intervals when possible: This maximizes our options for the future" is a key insight into why the greedy approach guarantees minimum removals.
# What this means:
# By selecting intervals that end earliest, you're freeing up more space on the timeline for potential future intervals. Think of it like this:
# Imagine you have two intervals that start at the same time but end at different times:

# Interval A: [1, 3]
# Interval B: [1, 5]

# If you choose Interval A (which ends earlier at 3), you can potentially add any interval that starts at 3 or later.
# If you choose Interval B (which ends later at 5), you can only add intervals that start at 5 or later.
# By choosing A, you've kept your options open for intervals starting at times 3 and 4, which you would have lost if you had chosen B.
# This principle applies throughout the entire sorted array - at each step, by choosing the interval that ends earliest (and doesn't overlap with what we've already chosen), we maximize the remaining time available for future intervals. This naturally leads to fitting in the maximum number of non-overlapping intervals, which means removing the minimum number of intervals.
# This is why sorting by end time (not start time) is crucial - it allows us to implement this greedy choice correctly.

# how to reach the conclusion that the intervals must be sorted by their endpoints. in greedy algo based questions, i sometimes see sorting by start time, sorting by end time, sum times length of interval etc. what is the way to think about these problems and in the first place how to know that the given problem needs a solution based on greedy algos
        