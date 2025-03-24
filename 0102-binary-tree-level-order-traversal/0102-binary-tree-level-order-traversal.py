# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level_order_traversal_list=[]
        queue=deque([root])
        while queue:
            k=len(queue)
            level_list=[]
            for _ in range(k):
                popped_node=queue.popleft()
                level_list.append(popped_node.val)
                if popped_node.left!=None:
                    queue.append(popped_node.left)
                if popped_node.right!=None:
                    queue.append(popped_node.right)
            level_order_traversal_list.append(level_list)
        return level_order_traversal_list

#a problem similar to calculating the max length of a binary tree
#the key is to keep calculating the length of the queue
        