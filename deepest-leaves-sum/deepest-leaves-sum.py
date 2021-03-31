# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        deq = deque()
        deq.append((root, 0))
        sum_of_curr_level = 0
        curr_level = 0
        while deq:
            node, level = deq.popleft()
            if level > curr_level:
                sum_of_curr_level = 0
                curr_level = level
            sum_of_curr_level += node.val
            if node.left: deq.append((node.left, curr_level + 1))
            if node.right: deq.append((node.right, curr_level + 1))
        
        return sum_of_curr_level
        
                
            
            
        
        
            