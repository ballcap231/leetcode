class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        
        def dfs(node):
            for count, val in enumerate(isConnected[node]):
                if val and count not in seen:
                    seen.add(count)
                    dfs(count)
        
        ans = 0
        for val in range(len(isConnected)):
            if val not in seen:
                dfs(val)
                ans += 1
        
        return ans