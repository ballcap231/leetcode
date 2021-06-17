from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        #O(|x| * |y|) time and O(|x| * |y|) space
        if not x and not y:
            return 0
        x,y = abs(x),abs(y)
        paths = [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1)]
        Q = deque([(xx, 1) for xx in paths])
        visited = set([(0,0)])
        
        while Q:
            curr,jumps = Q.popleft()
            if curr[0] == x and curr[1] == y:
                return jumps
            for path in paths:
                new_x = curr[0] + path[0]
                new_y = curr[1] + path[1]
                new_pos = (new_x,new_y)
                if new_pos not in visited:
                    Q.append((new_pos,jumps + 1))
                    visited.add(new_pos)
        
        # x, y = abs(x), abs(y)
        # if (x < y): x, y = y, x
        # if (x == 1 and y == 0): return 3        
        # if (x == 2 and y == 2): return 4        
        # delta = x - y
        # if (y > delta): return delta - 2 * int((delta - y) // 3);
        # else: return delta - 2 * int((delta - y) // 4);
        
        # @lru_cache(None) 
        # def dp(x,y):
        #     if x + y == 0: return 0
        #     elif x + y == 2: return 2
        #     elif x + y == 1: return 3
        #     return min(dp(abs(x-1),abs(y-2)), dp(abs(x-2),abs(y-1))) + 1
        # return dp(abs(x),abs(y))
                
            