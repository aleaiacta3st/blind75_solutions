def reverseList(head):
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
