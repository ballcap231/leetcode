class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #DFS - O(N) time and O(N) space
        #Graph theory - in order to be a valid tree, the number of 
        #edges in a graph must be equal to n - 1 where n is the number of
        #nodes. If there is less than n - 1, it is not fully connected,
        #if there is more than n - 1, there is a cycle.
        if len(edges) != n - 1: return False
        
        seen = {0}
        adj_matrix = defaultdict(list)
        for e_1, e_2 in edges:
            adj_matrix[e_1].append(e_2)
            adj_matrix[e_2].append(e_1)
            
        def dfs(root):
            for node in adj_matrix[root]:
                if node not in seen:
                    seen.add(node)
                    if root in adj_matrix:
                        dfs(node)
        dfs(0)
        return len(seen) == n
        
        
        
        
        
        
        
        #BFS
#         if len(edges) != n - 1: return False

#         # Create an adjacency list.
#         adj_list = [[] for _ in range(n)]
#         for A, B in edges:
#             adj_list[A].append(B)
#             adj_list[B].append(A)

#         # We still need a seen set to prevent our code from infinite
#         # looping if there *is* cycles (and on the trivial cycles!)
#         seen = {0}
#         queue = collections.deque([0])

#         while queue:
#             node = queue.popleft()
#             for neighbour in adj_list[node]:
#                 if neighbour in seen:
#                     continue
#                 seen.add(neighbour)
#                 queue.append(neighbour)

#         return len(seen) == n