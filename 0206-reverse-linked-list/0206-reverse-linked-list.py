# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None 
        current = head 
        while current is not None:
            temp = current.next #save the reference to the next node because 
                                #we are about to remake connections
            current.next = prev #make the current node point to its previous node
            prev=current #Move prev forward to current
            current = temp #Move current forward to temp
        return prev

     
# Both temp and current.next are references (or pointers) to ListNode objects 
# in memory, not the actual objects themselves.    

# A ListNode object is a structure in memory that contains:
# A value (val)
# A reference to another node (next)

# When we write temp = current.next:
# We're not copying the node
# We're just creating another reference to the same node
# Both temp and current.next point to the identical object in memory

# current and current.next point to different objects

# Essentially, we're iterating through the list, flipping each node's next 
# pointer to point to the previous node instead of the next node. 
# The temp variable ensures we don't lose our way forward after breaking '
# 'the original connections'