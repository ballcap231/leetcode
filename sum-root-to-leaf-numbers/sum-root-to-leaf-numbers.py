# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        self.sum = 0
        
        def dfs(node, num):
            if not node:
                return
            
            new_num = num * 10 + node.val
            if not node.left and not node.right:
                self.sum += new_num
            
            dfs(node.left, new_num)
            dfs(node.right, new_num)
        dfs(root, 0)
        return self.sum
        
        
        
        
        
        
        
        
        
        
        
        # #O(N) time and O(logN) space
        # def dfs(node, val):
        #     if not node:
        #         return
        #     val = val * 10 + node.val
        #     if not node.left and not node.right:
        #         self.sum += val
        #     else:
        #         dfs(node.left,val)
        #         dfs(node.right,val)
        # self.sum = 0
        # dfs(root, 0)
        # return self.sum
        
        
        #even worse time complexity
        # def dfs(node):
        #     if not node:
        #         return
        #     self.val += str(node.val)
        #     if not node.left and not node.right:
        #         self.sum += int(self.val)
        #     else:
        #         dfs(node.left)
        #         dfs(node.right)
        #     self.val = self.val[:-1]
        # self.sum = 0
        # self.val = ''
        # dfs(root)
        # return self.sum
        
        
        #O(NlogN) time and O(logN) space
        # def dfs(node):
        #     if not node:
        #         return
        #     self.stack.append(str(node.val))
        #     if not node.left and not node.right:
        #         self.sum += int(''.join(self.stack))
        #     else:
        #         dfs(node.left)
        #         dfs(node.right)
        #     self.stack.pop()    
        # self.sum = 0
        # self.stack = []
        # dfs(root)
        # return self.sum