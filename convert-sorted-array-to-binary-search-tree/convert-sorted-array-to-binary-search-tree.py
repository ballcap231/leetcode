# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def make_binary_subtree(left, right):
            if left > right:
                return None
            
            middle = (left + right) // 2
            
            middle_node = TreeNode(val=nums[middle])
            middle_node.left = make_binary_subtree(left, middle - 1)
            middle_node.right = make_binary_subtree(middle + 1, right)
            
            return middle_node
            
        return make_binary_subtree(0, len(nums) - 1)