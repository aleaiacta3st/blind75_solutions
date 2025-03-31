# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        hare = head 
        tort = head
        while hare is not None and hare.next is not None:
            hare = hare.next.next 
            tort = tort.next
            if (hare == tort):
                return True
        return False


# explain why and not or? explain why to check both hare and hare.next
# The Logical Necessity of "AND"
# With while hare is not None OR hare.next is not None:
#     If hare is not None (true) but hare.next IS None (false)
#     The OR condition still evaluates to TRUE
#     The code proceeds and attempts hare.next.next
#     This accesses a non-existent property of None → CRASH!
# With while hare is not None AND hare.next is not None:
#     BOTH conditions must be true to continue
#     This guarantees safe access to both pointers

# why dont we check if hare.next.next exists
# while hare is not None and hare.next is not None:
#     hare = hare.next.next
#     # Rest of code
# This two-part condition creates a protection perimeter that guarantees 
# safe access to hare.next.next because:
# hare is not None confirms the hare exists
# hare.next is not None confirms the first hop destination exists
# Once these conditions are met, hare.next.next will either be:
# A valid node (safe to access)
# None (also safe to access - signals end of list)






















        if not head:
            return False
        
        visited = set()  # Empty fortress to start
        current = head   # Begin the march from the head
        
        while current:
            if current in visited:  # Have we seen THIS soldier before?
                return True         # If yes, we've found a cycle
            visited.add(current)    # Mark THIS position as visited
            current = current.next  # March forward to next position
        
        return False  # Reached the end of the line - no cycle
        