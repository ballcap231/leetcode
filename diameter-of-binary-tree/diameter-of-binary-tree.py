# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.max_diam = 0
        if not root:
            return 0
        
        def dfs(node, diam):
            l_n, r_n = 0,0
            if node.left:
                l_n = dfs(node.left,diam + 1) + 1
            if node.right:
                r_n = dfs(node.right,diam + 1) + 1
                
            subtree_max = l_n + r_n
            self.max_diam = max(self.max_diam, subtree_max)
            return max(l_n,r_n)
        
        dfs(root,0)
        return self.max_diam