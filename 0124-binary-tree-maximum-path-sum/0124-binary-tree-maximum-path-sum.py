# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = [float('-inf')] 
        def dfs(root):
            if not root:
                return 0 
            left_gain = dfs(root.left)
            left_gain = max(0,left_gain)
            right_gain = dfs(root.right)
            right_gain=max(0,right_gain)
            max_path_sum[0]=max(max_path_sum[0], root.val+left_gain+right_gain)
            return (root.val+max(left_gain,right_gain))
        dfs(root)
        return max_path_sum[0]
        