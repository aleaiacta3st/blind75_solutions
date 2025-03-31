def hasCycle(head):
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
