class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        answer = []

        intervals.sort(key = lambda x:x[0])

        answer.append(intervals[0])

        for start,end in intervals[1:]:
            if start<= answer[-1][1]:
                answer[-1][1] = max(end, answer[-1][1])
            else:
                answer.append([start,end])

        return answer


        