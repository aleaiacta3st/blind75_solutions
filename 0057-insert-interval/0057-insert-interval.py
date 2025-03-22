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

        