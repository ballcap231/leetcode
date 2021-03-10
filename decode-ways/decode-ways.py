class Solution:
    def numDecodings(self, s: str) -> int:
        
#         @lru_cache(maxsize = None)
#         def dfs(start):
#             #postorder DFS
#             if start == len(s):
#                 return 1
#             if s[start] == '0':
#                 return 0
#             ret = 0
#             ret += dfs(start + 1)
#             if 10 <= int(s[start:start + 2]) <= 26:
#                 ret += dfs(start + 2)
#             return ret
#         return dfs(0)

        if not s:
            return 0
        dp = [0 for _ in range(len(s) + 1)]
    
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        
        for ii in range(2, len(dp)):
            
            if s[ii - 1] != '0':
                dp[ii] = dp[ii - 1]
            
            ints = int(s[ii-2: ii])
            if 10 <= ints <= 26:
                dp[ii] += dp[ii - 2]
            
        return dp[len(s)]
        