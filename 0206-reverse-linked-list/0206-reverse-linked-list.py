# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        def revlist(node):
            if node.next is None:
                return node
            store = revlist(node.next)
            node.next.next=node
            node.next=None 
            return store
        return revlist(head)

# The key insight: Each call reverses one connection while the overall 
# new head (original tail) propagates unchanged through the call stack.

# Observe that in every recursive call, you process exactly one node. 
# node.next.next=node
# The node next to the current node must now point to the current node
# node.next=None
# The current node now becomes tail. So make it point to next.

# During the middle of the recursive unwinding process, the list temporarily has 
# pointers going in two different directions. Consider a list 1→2→3→4:
# After the recursive call returns the reversed sublist (4→3→2), 
# but before we update the current node's connections, the list looks like:
# 1→2←3←4
# The current node (1) still points forward to 2, while 2 and beyond are already 
# reversed and pointing backward.
# Then we update the connections for node 1:
# Make 2 point to 1: node.next.next = node
# Break 1's forward connection: node.next = None'







#iteration based solution starts here

        # if head is None:
        #     return None
        # prev = None 
        # current = head 
        # while current is not None:
        #     temp = current.next #save the reference to the next node because 
        #                         #we are about to remake connections
        #     current.next = prev #make the current node point to its previous node
        #     prev=current #Move prev forward to current
        #     current = temp #Move current forward to temp
        # return prev

     
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