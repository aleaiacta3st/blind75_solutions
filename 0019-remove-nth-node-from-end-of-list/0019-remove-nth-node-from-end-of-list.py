# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next=head
        hare=head
        tort=dummy_head
        # Advance hare n steps
        for _ in range(n):
            hare = hare.next  # No need for conditional here as we know n is valid
        while hare is not None:
            hare=hare.next
            tort=tort.next
        tort.next = tort.next.next
        return dummy_head.next


# when hare reaches the final node of the list, tort is exactly one node before 
# the node that needs to be removed. This positioning is perfect for the 
# operation you need to perform:
# tort.next = tort.next.next

# tort.next.next
# (tort.next) - this is a refernce to the node next to tort which is 
# what we want to remove
# (tort.next).next - this is a refernce to the node that is next to tort.next

# tort is a reference to a node in your linked list (let's call it Node A)
# tort.next is accessing the next attribute of Node A, which is a reference to the
#  next node (Node B) - this is the node you want to remove
# tort.next.next is accessing the next attribute of Node B, which is a reference 
# to the node after it (Node C)

# tort.next = tort.next.next
# You are changing the next attribute of Node A to point directly to Node C, 
# effectively removing Node B from the linked list.

# This is the fundamental operation for removing a node from a singly linked list
#  - you can't directly delete a node, but you can make it unreachable by changing'
#  ' the connections.RetryClaude can make mistakes. Please double-check responses.
        