class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
#         #O(N * (maxJump - minJump)) time and O(N) space
#         if s[-1] != '0':
#             return False
        
#         @lru_cache(maxsize = None)
#         def DFS(pos):
#             if pos == len(s) - 1:
#                 return True
#             if s[pos] == '1':
#                 return False
#             for new_pos in reversed(range(pos + minJump, min(pos + maxJump + 1, len(s)))):
#                 if DFS(new_pos): return True
#             return False
        
#         return DFS(0)

        #O(N) time and O(N) space
        deq, farthest = deque([0]), 0
        
        while deq:
            pos = deq.popleft()
            start =  max(farthest + 1, pos + minJump)
            for new_pos in range(start, min(len(s), pos + maxJump + 1)):
                if s[new_pos] == '0':
                    deq.append(new_pos)
                    if new_pos == len(s) - 1:
                        return True
            farthest = max(farthest, pos + maxJump)
        return False
                    
            
            