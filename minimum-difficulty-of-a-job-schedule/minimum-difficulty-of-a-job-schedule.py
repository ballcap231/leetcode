class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        @lru_cache(None)
        def helper(index, day):
            if n - index < d - day + 1:
                return -1
            if day == d:
                return max(jobDifficulty[index:])
            difficulty = float('inf')
            current =  0
            for i in range(index, n - d + day + 1):
                current = max(current, jobDifficulty[i])
                next_day = helper(i + 1, day + 1)
                if next_day != -1:
                    difficulty = min(difficulty, current + next_day) 
            return difficulty          
        return helper(0, 1)