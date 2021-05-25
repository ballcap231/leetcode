class Solution:
    def fib(self, n: int) -> int:
        
        #divide and conquer (top down DP)
        @lru_cache(maxsize = None)
        def DAQ(num):
            if num == 1:
                return 1
            if num == 0:
                return 0
            return DAQ(num - 1) + DAQ(num - 2)
        return DAQ(n)
        
        
        #O(N) and O(N)
        #Bottom Up DP
#         if n < 1:
#             return 0
#         dp = [0 for _ in range(n + 1)]
#         dp[1] = 1
#         for val in range(2, len(dp)):
#             dp[val] = dp[val - 1] + dp[val - 2]
        
#         return dp[-1]
    
#         if n < 1:
#             return 0
#         dp = [0,1]
        
#         for val in range(2, n + 1):
#             val = sum(dp)
#             dp[0] = dp[1]
#             dp[1] = val
            
#         return dp[-1]
            