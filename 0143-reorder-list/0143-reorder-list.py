# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        hare=head
        tort=head 

        while hare and hare.next:
            hare=hare.next.next
            tort=tort.next

        curr=tort.next
        tort.next=None
        prev=None 

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        first=head
        second=prev

        while second:
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2

        
