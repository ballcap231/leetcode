class Solution:
    def fib(self, n: int) -> int:
        
        @lru_cache
        def DAQ(num):
            if num == 1:
                return 1
            if num == 0:
                return 0
            
            return DAQ(num - 1) + DAQ(num - 2)
        
        return DAQ(n)