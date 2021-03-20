# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def add_parents(node, parent = None):
            if node:
                node.parent = parent
                node.dist = 0
                add_parents(node.left, node)
                add_parents(node.right, node)
        add_parents(root)
        
        
        deq = deque()
        deq.append(target)
        ans = []
        seen = set()
        seen.add(target)
        while deq:
            curr_node = deq.popleft()
            if curr_node.dist == K:
                ans.append(curr_node.val)
            else:
                for node in (curr_node.parent, curr_node.left, curr_node.right):
                    if node and node not in seen:
                        node.dist = curr_node.dist + 1
                        deq.append(node)
                        seen.add(node)
        return ans
                    
                    
        