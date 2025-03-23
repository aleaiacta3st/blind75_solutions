# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True 
        if p==None or q==None:
            return False
        stack_p=[p]
        stack_q=[q]
        while stack_p and stack_q:
            popped_p=stack_p.pop()
            popped_q=stack_q.pop()
            if (popped_p==None and popped_q!=None):
                return False
            if (popped_p!=None and popped_q==None):
                return False
            if (popped_p!=None and popped_q!=None):
                if (popped_p.val!=popped_q.val):
                    return False
                else:
                    stack_p.append(popped_p.right)
                    stack_p.append(popped_p.left)
                    stack_q.append(popped_q.right)
                    stack_q.append(popped_q.left)
        return (len(stack_p)==len(stack_q))

#dfs with iteration
#make two stacks
# pop nodes
# compare values
# if equal, push their children into the stack.
# Don't worry is one of the children is None.'
# Because when None is popped, it falls into one the 
# if conditions and immediately returns False 
# we have only implicitly considered the case when 
# both popped nodes are none. In that case the structures 
# are still equal, but there is no point to adding them to the stack.
# we just saved some processing overhead. 

#the while loop stops when atleast one of the stacks is empty. 
# if a structure is deeper than the other, it may still be non-empty
# while the other stack is empty
# that is why as a final check we must verify that lengths of both 
# stacks is the same 
        
        
        
        
        
        
        
        
        
        
        
        
#dfs with recursion starts here        
        if p==None and q==None:
            return True 
        if p==None or q==None:
            return False
        if (p.val==q.val):
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False


# In Python:
# None is the Python keyword that represents the absence of a value.
# null does not exist. 


# Tree P
#     1
#    / \
#   2   3

# Tree Q 
#     1
#    / \
#   2   3


# isSameTree(1,1)
#    ├── isSameTree(2,2)
#    │       ├── isSameTree(None,None) → True
#    │       └── isSameTree(None,None) → True
#    └── isSameTree(3,3)
#            ├── isSameTree(None,None) → True
#            └── isSameTree(None,None) → True
        