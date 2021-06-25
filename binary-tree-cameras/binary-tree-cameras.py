# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        #Post-Order Greedy DFS
        #O(N) time and O(H) space
        self.count = 0
        covered = {None}
        
        def dfs(node, parent):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                
                if node.left not in covered or node.right not in covered:
                    self.count += 1
                    covered.update({node, parent, node.left, node.right})
        dfs(root, None)
        if root not in covered:
            self.count += 1
        return self.count
        