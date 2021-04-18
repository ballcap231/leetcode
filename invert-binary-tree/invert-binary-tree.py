# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

        
        
#         if not root:
#             return None
        
#         right = self.invertTree(root.right)
#         left = self.invertTree(root.left)
#         root.right = left
#         root.left = right
#         return root