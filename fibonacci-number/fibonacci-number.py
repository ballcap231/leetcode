class Solution:
    def fib(self, N: int) -> int:
        #O(N) time and O(1) space not using DP
        if N < 2:
            return N
        front,back = 1,0
        for ii in range(2, N + 1):
            front, back = back, front
            front = front + back
        return front

#         #O(N) time and O(N) space using iterative DP
#         self.hash_table = dict()
#         def recurse(N):
#             if N == 1:
#                 return 1
#             if N == 0:
#                 return 0
#             if N in self.hash_table:
#                 return self.hash_table[N]
#             self.hash_table[N] = recurse(N - 2) + recurse(N - 1)
#             return self.hash_table[N]
        
#         return recurse(N)

#         #O(N) time and O(N) space 
#         #using Recursive Divide & Conquer + Memoization (aka Top-Down DP)        
#         @lru_cache(maxsize = None)
#         def DivConq(n):
#             if n == 0:
#                 return 0
#             if n == 1:
#                 return 1
#             return DivConq(n - 1) + DivConq(n - 2)
#         return DivConq(N)
        