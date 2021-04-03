# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node, level):
        if node:
            # if level not in self.ans: self.ans[level] = node.val #works if we swap order of visiting right/left
            self.ans[level] = node.val
            self.DFS(node.left, level + 1)
            self.DFS(node.right, level + 1)
            
            
    def rightSideView(self, root: TreeNode) -> List[int]:
        #pre-order DFS - O(N) time, O(logN) space on average and O(N) worst case
        self.ans = {}
        self.DFS(root, 0)
        return list(self.ans.values())
            
            
            
            
            
        
        
        
        
        
        
        
        
#         #O(N) time and O(W) space where W is the largest width of the tree 
#         if not root: return []
#         ans = []
#         deq = deque()
#         deq.append((root, 0))
#         last_level = 0
        
#         while deq:
#             node, level = deq.popleft()
            
#             if level > last_level:
#                 ans.append(level_node.val)
#             last_level = level
#             level_node = node
#             if node.left: deq.append((node.left, level + 1))
#             if node.right: deq.append((node.right, level + 1))
        
#         ans.append(level_node.val)
#         return ans