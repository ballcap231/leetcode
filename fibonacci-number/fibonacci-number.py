class Solution:
    def fib(self, N: int) -> int:
        
        
        
        #O(N) time and O(N) space using iterative DP
        self.hash_table = dict()
        def recurse(N):
            if N == 1:
                return 1
            if N == 0:
                return 0
            if N in self.hash_table:
                return self.hash_table[N]
            self.hash_table[N] = recurse(N - 2) + recurse(N - 1)
            return self.hash_table[N]
        
        return recurse(N)