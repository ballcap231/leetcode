class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g, cnt, seen = collections.defaultdict(set), 0, set()
        for u, v in edges: 
            g[u].add(v), g[v].add(u)

        def dfs(node):
            if node not in seen:
                seen.add(node)
                for nei in g[node]: dfs(nei)
            return 1

        def bfs(q):
            for node in q:
                if node not in seen:
                    q += g[node]
                    seen.add(node)
            return 1

        # return sum(dfs(i) for i in range(n) if i not in seen)
        return sum(bfs([i]) for i in range(n) if i not in seen)        