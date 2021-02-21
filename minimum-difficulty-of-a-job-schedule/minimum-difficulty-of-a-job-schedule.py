class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        #O(|jobDifficulty| * |jobDifficulty| * d) time and O(|jobDifficulty| * d) space
        #Recursion + memoization
        if d > len(jobDifficulty):
            return -1
        
        min_diff = 0
        l = len(jobDifficulty)
        
        @lru_cache(maxsize = None)
        def recurse(start, day):
            if day == 1:
                return max(jobDifficulty[start:])
            day_max = 0
            min_diff = float('inf')
            for pos in range(start, l - day + 1):
                day_max = max(jobDifficulty[pos], day_max)
                min_diff = min(min_diff, day_max + recurse(pos + 1, day - 1))

            return min_diff
        return recurse(0, d)
    
