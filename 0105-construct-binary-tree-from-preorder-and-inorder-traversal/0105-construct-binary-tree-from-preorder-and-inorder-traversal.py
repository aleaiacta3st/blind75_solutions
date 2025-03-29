# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        inorder_set={}
        for i in range(n):
            inorder_set[inorder[i]]=i
        index = [0]
        def dfs(left,right):
            if left>right:
                return None
            root = TreeNode(preorder[index[0]])
            root_index = inorder_set[preorder[index[0]]]
            index[0]+=1
            root.left = dfs(left,root_index-1)
            root.right = dfs(root_index+1,right) 
            return root
        return dfs(0,n-1)
        