class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
#         #O(|jobDifficulty| * |jobDifficulty| * d) time and O(|jobDifficulty| * d) space
#         #Recursion + memoization
#         if d > len(jobDifficulty):
#             return -1
        
#         min_diff = 0
#         l = len(jobDifficulty)
        
#         @lru_cache(maxsize = None)
#         def recurse(start, day):
#             if day == 1:
#                 return max(jobDifficulty[start:])
#             day_max = 0
#             min_diff = float('inf')
#             for pos in range(start, l - day + 1):
#                 day_max = max(jobDifficulty[pos], day_max)
#                 min_diff = min(min_diff, day_max + recurse(pos + 1, day - 1))

#             return min_diff
#         return recurse(0, d)

#         #O(|jobDifficulty| * |jobDifficulty| * d) time and O(|jobDifficulty| * d) space
#         #Dynamic Programming
#         n = len(jobDifficulty)
#         if n < d:
#             return -1
        
#         dp = [[0] + [float('inf')] * n for _ in range(d + 1)]
        
#         for i in range(1, d + 1):
#             for j in range(i, n + 1):
#                 current = 0
#                 for k in range(j, i - 1, -1):
#                     current = max(current, jobDifficulty[k - 1])
#                     dp[i][j] = min(dp[i][j], current + dp[i - 1][k - 1])
#         return dp[-1][-1]

        #O(|jobDifficulty| * d) time and O(|jobDifficulty| * d) space
        #DP + stack
        A = jobDifficulty
        n = len(A)
        if n < d:
            return -1
        
        dp = [[0] + [float('inf')] * n for _ in range(d + 1)]
        
        for day in range(1, d + 1):
            stack = []
            for j in range(day, n + 1):
    			# schedule j at the dayth days
                dp[day][j] = dp[day - 1][j - 1] + A[j - 1] 
                while stack and A[stack[-1] - 1] <= A[j - 1]:
                    i = stack.pop()
					# find i such that A[i] <= A[j], then schedule i at the same day as j
                    dp[day][j] = min(dp[day][j], dp[day][i] - A[i - 1] + A[j - 1])
                if stack:
				    # j might not be the max, schedule j at the same day as the max
                    dp[day][j] = min(dp[day][j], dp[day][stack[-1]])
                stack.append(j)
        return dp[-1][-1]
    
