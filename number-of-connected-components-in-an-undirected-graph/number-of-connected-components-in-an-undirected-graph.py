class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #O(max(n,N)) time and O(N) space where N is length of edges
        dd = defaultdict(set)
        seen = set()
        for a, b in edges:
            dd[a].add(b)
            dd[b].add(a)
        
        def dfs(node):
            for ii in dd[node]:
                if ii not in seen:
                    seen.add(ii)
                    dfs(ii)
            return 1
        
        return sum(dfs(ii) for ii in range(n) if ii not in seen)
            
            
            