# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        stack = [(root,True)]
        res = []
        while stack:
            node, is_new = stack.pop()
            if is_new:
                if node.right:
                    stack.append((node.right,True))
                stack.append((node,False))
                if node.left:
                    stack.append((node.left,True))
            else:
                res.append(node.val)
        return res
        
        
#         ret = []
        
#         def traverse(node):
#             if node:
#                 traverse(node.left)
#                 ret.append(node.val)
#                 traverse(node.right)
        
#         traverse(root)
#         return ret