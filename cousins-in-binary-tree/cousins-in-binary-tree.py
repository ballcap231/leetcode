# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        #O(N) time and O(N) space
        if root and (root.val == x or root.val == y): return False
        
        def get_node_level(curr_node, search_node, parent_node=None, level = 0):
            if not curr_node: return None
            if curr_node.val == search_node:
                return (level, parent_node.val)
            return get_node_level(curr_node.left, search_node, curr_node, level + 1) or \
                            get_node_level(curr_node.right, search_node, curr_node, level + 1)

        x_level, x_parent = get_node_level(root, x)
        y_level, y_parent = get_node_level(root, y)
        return x_level == y_level and y_parent != x_parent