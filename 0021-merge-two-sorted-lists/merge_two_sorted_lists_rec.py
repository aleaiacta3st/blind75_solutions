def mergeTwoLists(list1,list2):

    def mergeTwoLists(list1, list2):
        def merge(p, q):
            # Base cases
            if p is None:
                return q
            if q is None:
                return p
            
            # Choose smaller value as current head
            if p.val < q.val:
                p.next = merge(p.next, q)
                return p
            else:
                q.next = merge(p, q.next)
                return q
        
        return merge(list1, list2)
    
            

# In your recursive implementation, p and q are indeed nodes - 
# they represent the current nodes from each linked list that you're '
# 'comparing at any given step of the recursion.
# When your merge function is first called:

# p initially represents the head of the first list
# q initially represents the head of the second list

# As the recursion progresses, these parameters represent whatever nodes in the two lists you're currently examining'
# ''

# Merge(p,q) returns the head of a sorted list 
# we compare p and q and add whichever is biggest to the front of the head that we 
# get back from the next recursive call


# you're thinking:

# “p will come before q later during recursion.”

# But here's the truth:

# The node you return now is the one that appears first in the final list.

# 📦 Think of each return as handing back a link in the chain.
# p = 2 → 4 → 6  
# q = 3 → 5 → 7

# merge(p, q)
# p.val < q.val → so you say:
# p.next = merge(p.next, q)
# return p

# That means:

# You pick p now (2)

# You tell p.next to be the result of merging the rest

# And you return p upward

# So 2 becomes the first node in the final list. ✅
