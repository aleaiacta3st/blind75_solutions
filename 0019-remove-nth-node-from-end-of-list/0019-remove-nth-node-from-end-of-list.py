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

# The dummy node (or sentinel node) is a critical technique in 
# linked list operations that serves several important purposes:

# Handling edge cases elegantly: Without a dummy node, removing the head of a 
# list would require special handling, as there's no previous node to modify. '
# 'The dummy node ensures there's always a node before any potential removal target.

# Uniform code path: By using a dummy node, you don't need separate if/else branches'
# ' for removing the head versus other nodes. This makes your code cleaner and less'
# ' error-prone.
# Return value simplification: Instead of tracking if you removed the head and 
# conditionally returning a new head, you can always simply return dummy.next as 
# your new head.

# In your specific solution, this is particularly important because:

# If the nth node from the end happens to be the head
# When using the two-pointer approach, you need the second pointer to stop one 
# position before the node to be removed

# Without the dummy node, you'd have no way to position a pointer before the '
# 'head if that's the node that needs to be removed.

# This pattern appears frequently in linked list problems where modifications to 
# the list structure are required. It's a simple technique but incredibly powerful'
# ' for simplifying linked list manipulations.    
        