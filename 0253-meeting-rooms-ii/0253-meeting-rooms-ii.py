class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        
        rooms = 0
        e = 0  # end pointer
        
        for s in range(len(starts)):
            if starts[s] < ends[e]:
                rooms += 1  # need new room
            else:
                e += 1  # a room freed up, reuse it
        
        return rooms

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
        