# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(p, q):
            # Base cases
            if p is None:
                return q
            if q is None:
                return p
            
            # Choose smaller value as current head
            if p.val < q.val:
                p.next = merge(p.next, q)
                return p
            else:
                q.next = merge(p, q.next)
                return q
            
        def mergemulti(q):
            n=len(q)
            if n==0:
                return None
            if n==1:
                return q[0]
            mid =n//2
            l1 = mergemulti(q[0:mid])
            l2 = mergemulti(q[mid:n])
            return merge(l1,l2) 
        return mergemulti(lists)
    
#     You can't return mergemulti(l1, l2) because of a parameter mismatch:

# mergemulti expects one parameter: a list of linked lists (q)
# merge expects two parameters: two individual linked lists (l1, l2)

# When you reach the point where you have two merged sublists, you need to combine 
# them with the function specifically designed for merging two lists - your original merge function.

# mergemulti can work with mid/2 elements and give back 1 sorted list 
# make 2 lists 
# use your merge 2 list function to merge them

# Fix: Changed list division from [0:mid+1] and [mid+1:n] to [0:mid] and [mid:n]
# Original approach caused infinite recursion with 2 elements because [0:mid+1] 
# returned the entire list again rather than reducing problem size.
# Proper division ensures each recursive call gets strictly fewer elements.

# Your Original Approach (causing infinite recursion):
# mid = n//2  # For n=2, mid=1
# l1 = mergemulti(q[0:mid+1])  # q[0:2] - This is STILL the entire list!
# l2 = mergemulti(q[mid+1:n])  # q[2:2] - This is an empty list

# When you have exactly 2 elements:
# Your first recursive call gets the ENTIRE list again (not reducing the problem)
# The function keeps calling itself with the same 2-element input forever

# mid = n//2  # For n=2, mid=1
# l1 = mergemulti(q[0:mid])  # q[0:1] - Just the first element
# l2 = mergemulti(q[mid:n])  # q[1:2] - Just the second element

# With 2 elements:
# First recursive call gets 1 element
# Second recursive call gets 1 element
# Both reach the base case n==1 immediately after

# For a recursive algorithm to terminate, each recursive call must work 
# with a strictly smaller problem than the original. The key insight is finding 
# a division that guarantees reduction in problem size with every call - 
# which [0:mid] and [mid:n] accomplishes by creating two non-overlapping, 
# smaller lists.
# This is a common pitfall in divide-and-conquer algorithms - always ensure your 
# division strategy actually reduces the problem size!
    
        