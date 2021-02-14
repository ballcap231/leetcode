from collections import deque
import itertools
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
#         if not x and not y:
#             return 0
#         p_1,p_2 = [1,-1],[2,-2]
#         paths = list(itertools.product(p_1,p_2)) + list(itertools.product(p_2,p_1))
#         self.Q = deque([(xx, 1) for xx in paths])
        
#         while self.Q:
#             curr,jumps = self.Q.popleft()
#             if curr[0] == x and curr[1] == y:
#                 return jumps
#             for path in paths:
#                 self.Q.append(((curr[0] + path[0], curr[1] + path[1]),jumps + 1))

        @lru_cache(None) 
        def dp(x,y):
            if x + y == 0: return 0
            elif x + y == 2: return 2
            elif x + y == 1: return 3
            return min(dp(abs(x-1),abs(y-2)), dp(abs(x-2),abs(y-1))) + 1
        return dp(abs(x),abs(y))
                
            