# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten_node(self, node):
        if not node or not node.left and not node.right:
            return node
        
        left_flat = self.flatten_node(node.left)
        right_flat = self.flatten_node(node.right)
        
        if left_flat:
            left_flat.right = node.right
            node.right = node.left
            node.left = None
        
        return right_flat if right_flat else left_flat
        
        
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_node(root) 
            