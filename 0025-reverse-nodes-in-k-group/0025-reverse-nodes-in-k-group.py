# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        group_prev=dummy 


        while True:
            kth=group_prev
            for _ in range(k):
                kth=kth.next
                if kth is None:
                    return dummy.next 

            group_next=kth.next

            prev=group_next
            curr=group_prev.next

            for _ in range(k):
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt 


            tmp=group_prev.next
            group_prev.next=prev
            group_prev=tmp 

        
        return dummy.next


        