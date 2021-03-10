class Solution:
    def numDecodings(self, s: str) -> int:
        #Top Down DP solution - O(N) and O(N)
        @lru_cache(maxsize = None)
        def dfs(start):
            #postorder DFS
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
        
        #Bottom Up DP Solution - O(N) and O(N)
#         if not s:
#             return 0
#         dp = [0 for _ in range(len(s) + 1)]
#         dp[0] = 1
#         dp[1] = 1 if s[0] != '0' else 0
#         for ii in range(2, len(dp)):
#             if s[ii - 1] != '0':
#                 dp[ii] = dp[ii - 1]
            
#             ints = int(s[ii-2: ii])
#             if 10 <= ints <= 26:
#                 dp[ii] += dp[ii - 2]    
#         return dp[-1]
        
        #Bottom Up DP Solution - O(N) time and O(1) time
        if not s or s[0] == '0':
            return 0
        dp = [1,1]
        for ii in range(2, len(s) + 1):
            temp = 0
            if s[ii - 1] != '0':
                temp += dp[1]
            double_digit = int(s[ii - 2 : ii])
            if double_digit >= 10 and double_digit <= 26:
                temp += dp[0]
            dp = [dp[1],temp]
        return dp[-1]
        