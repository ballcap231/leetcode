# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.global_max = root.val
        
        def dfs(node):
            local_max = node.val
            if node.left:
                left_max = dfs(node.left)
                local_max = max(local_max, left_max + node.val)
            if node.right:
                right_max = dfs(node.right)
                local_max = max(local_max, right_max + node.val)
            if node.left and node.right:
                self.global_max = max(self.global_max, node.val + left_max + right_max, local_max)
            else:
                self.global_max = max(self.global_max, local_max)
            
            return local_max 
            
            
        dfs(root)
        return self.global_max
            
            
            
            