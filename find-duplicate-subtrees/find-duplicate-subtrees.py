# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        #O(N) time and O(N) space
        trees = defaultdict()
        trees.default_factory = trees.__len__
        counts = Counter()
        ans = []
        
        def dfs(node):
            if node:
                node_id = trees[(node.val, dfs(node.left), dfs(node.right))]
                counts[node_id] += 1
                if counts[node_id] == 2:
                    ans.append(node)
                return node_id
        dfs(root)
        return ans
            
                