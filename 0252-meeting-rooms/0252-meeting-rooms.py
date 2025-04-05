class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        new_intervals_sorted=sorted(intervals)
        n=len(new_intervals_sorted)
        for i in range(n):
            if i!=n-1 and new_intervals_sorted[i][1] > new_intervals_sorted[i+1][0]:
                return False 
        return True


# sort in increasing order of start times 
# if the next meeting starts before the previous meeting ends, return False 
# the last element does not have an element next to it to make a comparison. so watch out for that edge case.

        