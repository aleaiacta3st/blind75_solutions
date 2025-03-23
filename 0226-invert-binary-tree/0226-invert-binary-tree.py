# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root 
        if (root.left==None and root.right==None):
            return root 
        else:
            root.left,root.right=root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
             
        
        
    # bfs with iteration    
    #     if not root:
    #         return root 
    #     queue=deque([root])
    #     while queue:
    #         popped_node=queue.popleft()
    #         if popped_node!=None:
    #             temp=popped_node.left 
    #             popped_node.left=popped_node.right
    #             popped_node.right=temp
    #             queue.append(popped_node.left)
    #             queue.append(popped_node.right)
    #     return root
        
# Using bfs, going layer by layer
# create a queue
# pop a node 
# swap left and right if node is not None 
# Queue the children nodes AFTER swapping
# If you draw a simple tree and observe, you will find 
# that queuing AFTER swapping left and right values 
# inverts the structure of a tree

# When you enqueue after swapping:
# You’ve already inverted the children.
# Now you’re saying: "Here’s the new left and right children — "
# "go forth and invert their subtrees as well."
# The queue always holds the correct current structure, step by step.