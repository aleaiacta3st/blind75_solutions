# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index=0

        inorder_dict={val:idx for idx,val in enumerate(inorder)}

        def build(left,right):
            nonlocal index
            if left>right:
                return None 

            node=TreeNode(preorder[index])

            mid=inorder_dict[preorder[index]]

            index=index+1 

            node.left=build(left,mid-1)

            node.right=build(mid+1,right)

            return node 

        return build(0,len(inorder)-1)

            
            

        