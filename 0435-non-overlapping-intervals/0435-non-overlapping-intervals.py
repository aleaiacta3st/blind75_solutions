class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[1])

        n=len(intervals)

        last_end = intervals[0][1]

        count=1

        for i in range(1,n):
            if intervals[i][0] >= last_end:
                count=count+1
                last_end= intervals[i][1]

        result = len(intervals)-count

        return result
        