class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        max_rooms=0
        current_rooms=0
        starts=[]
        ends=[]
        for i in range(n):
            starts.append(intervals[i][0])
        for i in range(n):
            ends.append(intervals[i][1])
        starts.sort()
        ends.sort()
        start_pointer=0
        end_pointer=0
        while start_pointer<=n-1:
            if starts[start_pointer]<ends[end_pointer]:
                current_rooms+=1
                if current_rooms>max_rooms:
                    max_rooms=current_rooms
                start_pointer+=1
            else:
                current_rooms-=1
                end_pointer+=1
        return max_rooms
        