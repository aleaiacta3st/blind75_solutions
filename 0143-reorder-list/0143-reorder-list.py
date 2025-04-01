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
        if not head:
            return
            
        # Find the middle of linked list using hare/tortoise
        tort = hare = head
        while hare and hare.next:
            tort = tort.next
            hare = hare.next.next
        
        # Reverse the second part of the list
        curr_second_list = tort
        prev = None
        while curr_second_list:
            # Save next pointer before changing it
            temp = curr_second_list.next
            # Reverse the pointer
            curr_second_list.next = prev
            # Move prev forward
            prev = curr_second_list
            # Move current to saved next
            curr_second_list = temp
        
        # Merge two halves
        first = head
        second = prev
        while second.next:  # This condition ensures we handle the last node correctly
            # Save next pointers before changing them
            temp1 = first.next
            temp2 = second.next
            
            # Connect first to second
            first.next = second
            # Connect second to next of first
            second.next = temp1
            
            # Move pointers forward using saved next values
            first = temp1
            second = temp2

        