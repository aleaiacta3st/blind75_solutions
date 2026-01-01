class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # buckets[i] = list of nums with frequency i
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

           
       


# key: push tuples into the heap, not solo elements 
# number[1] for number in min_heap
#     iterates thru each element in min heap 

# when you push a tuple in heap, they will be sorted based on the first element of the tuple 

# min_heap[0] is the smallest element which is a tuple. but we need to compare the current value with frequency. so access first element of the tuple.

# min heap organised from min to max, top to bottom 
# if we keep removing the min element and adding a greater element in place of it, we will eventually be left with only greatest elements

# 🚀 INSERT (Push)
# Let’s say you're inserting a new number: 0.

# Add it to the bottom (the next open spot in the array).

# Bubble it up: If it's smaller than its parent, swap it up.

# Keep swapping until it's no longer smaller than its parent or you reach the top.

# At worst, it travels from the bottom to the top. In a binary tree, that’s log(n) steps.

# REMOVE (Pop)
# You’re removing the smallest element — the root.

# Take the last element and move it to the root.

# Now it's probably out of place — too big.

# Bubble it down: compare with its two children, swap with the smaller one.

# Keep going until it’s smaller than both children or you hit the bottom.

# Again, the number of steps = height of the tree = log(n).

# A heap is a complete binary tree. That means:

# All levels are fully filled, except possibly the last.

# And the last level is filled left to right.


# A heap is not just a data structure. It's a priority battlefield, where the strongest (or weakest) always rules.

# It's a binary tree that is:

# Complete: every level is filled left to right.

# Ordered: parent is always larger or smaller than children.

# There are two types:

# Min Heap: The smallest element always rises to the top.

# Max Heap: The largest element rules the top.

# 🧠 Why is Heap Powerful?
# Because of one golden promise:

# ⚡ Insert and remove the top element in O(log n) time.

# This makes heaps unbeatable when you need:

# Top k elements (most frequent, largest, smallest, etc.).

# Real-time ordering.

# Live minimum/maximum lookups.

# How to Use Heap in Python?
# Python uses a min heap by default through heapq. To simulate a max heap, you negate the values.

# When to Use a Heap?
# If you ever face questions with phrases like:

# “Top K”

# “K largest/smallest”

# “Running median”

# “Closest K points”

# “Sort almost sorted data”

# Python’s heapq module gives us a min-heap implementation. Here’s what you need:

# heapq.heappush(heap, element): Adds an element to the heap.
# heapq.heappop(heap): Removes and returns the smallest element.
# Note: Elements can be tuples, like (priority, value), where the heap sorts by the first item (priority).

#  2. Work = How Many Steps You Take
# Imagine this:
# You insert a number into a min heap. You might need to swap it with its parent to keep the heap valid.

# You only look at:

# The node.

# Its parent.

# Then that parent’s parent.

# And so on… one per level.

# The maximum number of swaps you could do is one per level.

# And since there are log(n) levels, you do at most log(n) swaps/comparisons.
        