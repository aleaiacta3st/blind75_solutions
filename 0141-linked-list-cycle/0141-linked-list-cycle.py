# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
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
        