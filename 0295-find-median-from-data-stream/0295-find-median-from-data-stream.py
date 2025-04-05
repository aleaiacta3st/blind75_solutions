class MedianFinder:

    def __init__(self):
        self.min_heap=[]
        self.max_heap=[]

        

    def addNum(self, num: int) -> None:
        if len(self.max_heap)!=0 and num<-self.max_heap[0]:
            heapq.heappush(self.max_heap,-num)
        else:
            heapq.heappush(self.min_heap,num)
        if abs (len(self.max_heap)-len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap):
                heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
            else:
                heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
        if self.max_heap and self.min_heap and not -self.max_heap[0]<self.min_heap[0]:
            a=heapq.heappop(self.max_heap)# Extract negative value from max heap
            b=heapq.heappop(self.min_heap)# Extract positive value from min heap
            heapq.heappush(self.min_heap,-a)# Convert negative back to positive for min heap
            heapq.heappush(self.max_heap,-b)# Convert positive to negative for max heap
        

    def findMedian(self) -> float:
        if len(self.max_heap)==len(self.min_heap):
            return (-self.max_heap[0]+self.min_heap[0])/2 
        elif len(self.max_heap)>len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# self.max_heap[0],self.min_heap[0]=-self.min_heap[0],-self.max_heap[0]
# this is wrong. you cannot directly swap because the min and max positions in heaps are always the result of internal arrangements



# The max-heap should have the same number of elements as the min-heap or one more. That keeps the "middle" element at the top of the max-heap when the total is odd.

# once you balance both the heaps. you need to check if the rule of max of max heap is still less than the min of min heap. During balancing, this condition might break. so do a check and if broken, put the top elements in the other heap.

# if max heap and min heaps are not of same lengths, then whichever has the greater length contains the median at its top

# You're tasked with implementing a data structure that can efficiently:
# Accept a continuous stream of numbers
# Calculate the current median at any point in time

# The difficulty lies in maintaining an efficient structure as the stream grows. Consider these scenarios:
# Stream so far: [2]
# Current median: 2

# Stream so far: [2,3]
# Current median: (2+3)/2 = 2.5

# Stream so far: [2,3,4]
# Current median: 3

# A naive approach would store all elements and sort them each time we need the median - but that would be extremely inefficient. You need a structure that maintains order while allowing efficient insertions.

# Here’s the first principles truth:
# The median is the number that sits in the middle of a sorted list.
# It divides the list such that half the elements are smaller and half are larger.


# where are the min heap and min heap being used? arent they seen by the user
# Understanding MedianFinder's Implementation
# The min_heap and max_heap are internal implementation details - the user never directly interacts with them. This is a key concept in object-oriented programming called encapsulation.
# How It Works Internally:
# class MedianFinder:
#     def __init__(self):
#         self.min_heap = []  # Stores larger half of numbers
#         self.max_heap = []  # Stores smaller half of numbers (as negatives)
# These heaps are maintained internally by your class methods. Users of your class never need to:

# Create the heaps themselves
# Access the heaps directly
# Understand how the heaps store the data

# User's Perspective:
# From a user's perspective, they only interact with two methods:
# # User code
# finder = MedianFinder()  # Creates a new finder with empty heaps
# finder.addNum(41)        # User adds numbers one by one
# finder.addNum(35)
# current_median = finder.findMedian()  # User gets the current median
# The user doesn't need to know:

# That you're using heaps at all
# That the max_heap stores negative values
# How you balance the heaps
# Any other implementation details

# This abstraction is what makes your class powerful - the complexity of efficient median calculation is hidden behind a simple, clean interface that any developer can use without understanding the underlying mechanics.