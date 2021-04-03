# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #O(N) time and O(H) space - postorder DFS
        if not root: return 0
        self.global_max = 0
        def dfs(node):
            if node:
                l_max = dfs(node.left)
                r_max = dfs(node.right)
                
                self.global_max = max(self.global_max, l_max + r_max)
                local_max = max(l_max, r_max)
                return local_max + 1
            return 0
        
        dfs(root)
        return self.global_max