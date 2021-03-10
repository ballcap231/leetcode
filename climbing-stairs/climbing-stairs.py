class Solution:
    def climbStairs(self, n: int) -> int:

        @lru_cache(maxsize = None)
        def recurse(n):
            if n == 1:
                return 1
            if n == 2:
                return 2

            return recurse(n - 1) + recurse(n - 2)
        
        return recurse(n)