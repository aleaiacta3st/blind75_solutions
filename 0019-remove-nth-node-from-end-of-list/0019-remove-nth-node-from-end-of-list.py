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
        