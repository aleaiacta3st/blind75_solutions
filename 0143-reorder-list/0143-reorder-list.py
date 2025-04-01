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

        
# Confusion: “In the final merge loop, the middle or last node appears
# ‘dangling’—especially in the odd-length case—and it seems like we 
# lose track of it. How is it re-attached?”
# We never sever the link from the first half’s last node to the middle node 
# until we replace it with a connection to the reversed half.

# For an odd-length list, that “extra” middle node belongs to the first half, 
# so the reversed portion is shorter. We stop weaving once second.next is null, 
# which naturally keeps the middle node in place.

# No node truly “dangles” because we only overwrite pointers in a 
# controlled manner—enough to interlace the two halves without discarding 
# that middle node.


# the key is while second.next condition
# The loop condition while second.next: is a clever approach that 
# handles both even and odd-length lists elegantly.    

# A handy way to see it is that we never actually broke 2 → 3 during the weaving. 
# After reversing the half that starts at 3, node 2 is still pointing at node 3; 
# that link doesn’t get overwritten in the “merge” loop.

# On the first weave‐iteration, you do:
# first.next = second → makes 1 → 4
# second.next = temp1 → makes 4 → 2
# But you do not change 2 → 3.
# So when the loop sees that second.next (i.e. 3.next) is null, it stops and 
# never overwrites 2 → 3. The node 3 “looks” like it’s “hanging” there, but in 
# reality it’s still connected through the original pointer from node 2. 
# That’s why the final list is 1 → 4 → 2 → 3 with no nodes left dangling.

# Odd case 1 2 3 4 5

# Let’s do the second half of the merge step by step for the 
# odd list [1, 2, 3, 4, 5]. The key is realizing we never explicitly “sever” 
# the pointer from 2 to 3 until we finally redirect 2 to 4 
# in the second weave iteration. At the end, node 3 is tucked in naturally.

# etup
# Original list: 1 → 2 → 3 → 4 → 5

# We locate the middle (3) with tortoise/hare.

# Reverse from 3 onward: the sub-list [3, 4, 5] becomes 5 → 4 → 3.

# So now we have:

# “First half” (still pointing): 1 → 2 → 3

# “Second half” (reversed): 5 → 4 → 3 → null

# Important: notice we never cut 2 → 3; it’s still there. 
# But 3 now also has 4 → 3 behind it because we reversed that sub-chain.

# first = head       # first = 1
# second = prev      # second = 5   (start of the reversed half)

# Merge Iteration 1
# Goal: weave 1 with 5.

# temp1 = first.next
# → temp1 = 2

# temp2 = second.next
# → temp2 = 4

# first.next = second
# → 1 → 5

# second.next = temp1
# → 5 → 2

# So after iteration 1, the visible chain from the head is now:
# 1 → 5 → 2 → 3 → 4 → 5 ...
# (We won’t worry that we “see” multiple routes to node 5, because in the next steps we overwrite some links.)

# Finally we move first and second forward:
# first = temp1    # first = 2
# second = temp2   # second = 4

# Merge Iteration 2
# Now we weave 2 with 4.

# temp1 = first.next
# → temp1 = 3 (because originally 2 → 3)

# temp2 = second.next
# → temp2 = 3 (because reversed chain had 4 → 3)

# first.next = second
# → 2 → 4 (This overwrites the old pointer 2 → 3, so now 2 no longer points to 3; it points to 4.)

# second.next = temp1
# → 4 → 3 (That was already 4 → 3 from the reversed chain, but we confirm it.)

# So now the definitive chain is:
# 1 → 5 → 2 → 4 → 3 → null

# We move our pointers again:
# first = temp1    # first = 3
# second = temp2   # second = 3
# Stopping Condition
# Now second is at 3, and 3.next is null. The loop says while second.next:, 
# so we stop. No more weaving. The result is exactly:
# 1 → 5 → 2 → 4 → 3

# No node is “dangling.” Node 3 ends up last because we overwrote 
# the original 2 → 3 pointer at the right time, and the reversed links 
# placed 3 behind 4

# The usual approach in Reorder List is to let the first half have one more node 
# for odd lengths, but your snippet does the opposite (which also works). 
# The key is that only one half will hold that middle node—whichever half you 
# assign it to is simply a design choice, so long as you handle pointers correctly.