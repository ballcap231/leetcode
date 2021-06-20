# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.closest_val = root.val
        def dfs(node):
            if not node:
                return self.closest_val
            if node.val == target:
                return node.val
            if abs(node.val - target) < abs(self.closest_val - target):
                self.closest_val = node.val
            if node.val > target:
                return dfs(node.left)
            else:
                return dfs(node.right)
        return dfs(root)
                
                