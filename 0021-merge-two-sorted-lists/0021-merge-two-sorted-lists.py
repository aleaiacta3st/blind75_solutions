# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1 
        p2 = list2
        dummy_head = ListNode()
        tail = dummy_head
        while p1 is not None and p2 is not None:
            if p1.val < p2.val :
                tail.next = p1 #sets next value
                tail = tail.next #shifts focus
                p1=p1.next
            else:
                tail.next = p2
                tail = tail.next
                p2=p2.next
        if p1 is not None:
            tail.next=p1
        if p2 is not None:
            tail.next=p2
        return dummy_head.next
    

# The insight to initialize tail = dummy_head comes from understanding the 
# fundamental pattern of building linked lists with a dummy head node.
# Think of it this way:

# Purpose of the dummy head: The dummy head serves as an anchor point that exists
# before your actual list begins. It solves the "empty list" special case and
# simplifies your code by giving you a starting point that always exists.
# The tail's role: The tail pointer tracks the end of your growing list where '
# 'you'll add the next node.
# Initial state: At the very beginning, your list is empty except for the 
# dummy head. So logically, the last node (tail) of this nearly-empty list 
# IS the dummy head itself.

# This pattern appears in almost every linked list construction problem:

# Create a dummy head
# Initialize tail to point to this dummy head
# Build your list by setting tail.next and advancing tail
# Return dummy_head.next as your result

# You'll recognize that this pattern is appropriate whenever:

# You're building a linked list from scratch
# You need to handle an initially empty result list
# You want to avoid special case logic for the first insertion
    


# When you do tail.next = p1, you're setting the "next" pointer of the node '
# 'that tail references to point to p1.
# When you do tail = tail.next, you're changing what tail itself points to - '
# 'it now points to the same node that p1 points to.'
# ''
# both tail and dummyhead initially reference to the same object in memory. 
# just yes/no
# Yes, that's exactly right! Both tail and dummy_head initially reference the '
# 'same ListNode object in memory.'
# ''
# then when i do tail.next - tail is pointing to something else. tail cannot 
# point to both dummy head and to something else at the same time? i dont get it.
# There are two distinct operations happening with tail:

# Setting a property on the object tail points to:

# When you do tail.next = p1, you're modifying the next property of the node '
# 'that tail currently points to. You're not changing what tail itself points to.
# At this moment, both tail and dummy_head still point to the same node.


# Changing what tail points to:

# When you do tail = tail.next, you're reassigning the tail variable itself to '
# 'point to a different node.
# After this line, tail and dummy_head point to different nodes.

# It's like this:

# Initially, dummy_head and tail both hold the address of the same object
# tail.next = p1 modifies that object (it now has a "next" pointer)
# tail = tail.next moves tail to point to p1
# dummy_head remains pointing to the original node

# This is why the pattern works - dummy_head stays anchored at the beginning, 
# while tail advances through the list. 

        