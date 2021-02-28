# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        par_maps = dict()
        def dfs_annotate_parents(node, parent = None):
            if node:
                par_maps[node] = parent
                dfs_annotate_parents(node.left, node)
                dfs_annotate_parents(node.right, node)
            
        dfs_annotate_parents(root)
        
        dq = deque()
        dq.append((target,0))
        seen = {target}
        while dq:
            if dq[0][1] == K:
                return [n.val for n,d in dq]
            node, dist = dq.popleft()
            
            for neighbor in (node.left, node.right, par_maps[node]):
                if neighbor and neighbor not in seen:
                    dq.append((neighbor, dist + 1))
                    seen.add(neighbor)
        return []
            
            