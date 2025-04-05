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

# separate start times and end times into separate arrays
# get two pointers
# compare start with end
# if less, it means another meeting started 
#  add a room 
#  otherwise, decrease the current rooms 
#  while start_pointer<=n-1
#  it is enough if start pointer reaches the end, we need not wait for all end times also to be processed. 
#  because no new meeting is going to get started. rooms in use are only going to decrease from that point on.


#  if meetings overlap, they need separate rooms.
# This problem is about finding the maximum number of overlapping intervals at any point in time.
        