class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #O(N + n) time and O(N) space where N is length of edges
        #using DFS or BFS
        dd = defaultdict(set)
        seen = set()
        for a, b in edges:
            dd[a].add(b)
            dd[b].add(a)
        
        def dfs(node):
            seen.add(node)
            for ii in dd[node]:
                if ii not in seen:
                    seen.add(ii)
                    dfs(ii)
            return 1
        
        return sum(dfs(ii) for ii in range(n) if ii not in seen)
    
    
#         def bfs(node):
#             seen.add(node)
#             qq = deque(dd[node])
#             while qq:
#                 nn = qq.popleft()
#                 if nn not in seen:
#                     seen.add(nn)
#                     for jj in dd[nn]: qq.append(jj)
#             return 1
        
#         return sum(bfs(ii) for ii in range(n) if ii not in seen)
        
            
            
            