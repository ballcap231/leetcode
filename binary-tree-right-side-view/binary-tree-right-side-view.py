# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #O(N) time and O(W) space where W is the largest width of the tree 
        if not root: return []
        ans = []
        deq = deque()
        deq.append((root, 0))
        last_level = 0
        
        while deq:
            node, level = deq.popleft()
            
            if level > last_level:
                ans.append(level_node.val)
            last_level = level
            level_node = node
            if node.left: deq.append((node.left, level + 1))
            if node.right: deq.append((node.right, level + 1))
        
        ans.append(level_node.val)
        return ans
        
        
        
#         queue = deque()
#         queue.append(root)
#         outPut = []
        
#         while queue:
#             n = len(queue)
#             currLevel = []
#             for _ in range(n):
#                 node = queue.popleft()
#                 currLevel.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             outPut.append(currLevel[-1])
#         return outPut