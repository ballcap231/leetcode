# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        #O(H) time if unbalanced tree and O(logH) if balanced tree and O(1) space
        #Iterative DFS or Binary Search?
        self.closest_val = root.val
        curr_node = root
        while curr_node:
            if curr_node.val == target:
                return curr_node.val
            if abs(target - curr_node.val) < abs(target - self.closest_val):
                self.closest_val = curr_node.val
            if curr_node.val < target:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        return self.closest_val
        

                
                