class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(maxsize = None)
        def dfs(start):
            if start == len(s):
                return 1
            
            if s[start] == '0':
                return 0
            
            ret = 0
            
            ret += dfs(start + 1)
            
            if 10 <= int(s[start:start + 2]) <= 26:
                ret += dfs(start + 2)
            
            return ret
        
        return dfs(0)