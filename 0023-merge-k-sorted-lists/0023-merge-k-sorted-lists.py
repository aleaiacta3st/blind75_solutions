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
        