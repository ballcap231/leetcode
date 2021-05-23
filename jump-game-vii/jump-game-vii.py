class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
#         if s[-1] != '0':
#             return False
        
#         @lru_cache(maxsize = None)
#         def DFS(pos):
#             if pos == len(s) - 1:
#                 return s[pos] == '0'
#             if s[pos] == '1':
#                 return False
#             for new_pos in reversed(range(pos + minJump, min(pos + maxJump + 1, len(s)))):
#                 if DFS(new_pos): return True
#             return False
        
#         return DFS(0)
    
        q, farthest = deque([0]), 0
        
        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            for j in range(start, min(len(s), i + maxJump + 1)):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) - 1:
                        return True
            farthest = max(farthest, i + maxJump)
        return False