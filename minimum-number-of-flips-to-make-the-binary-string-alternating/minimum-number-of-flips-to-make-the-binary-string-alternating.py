class Solution:
    def minFlips(self, s: str) -> int:
        l = len(s)
        s_new = s * 2
        opt_1 = '01' * l
        opt_2 = '10' * l
        min_flip = len(s)
        min_1 = min_2 = 0
        for pos in range(len(s_new)):
            if s_new[pos] != opt_1[pos]:
                min_1 += 1
            if s_new[pos] != opt_2[pos]:
                min_2 += 1
            if pos >= l:
                if s_new[pos - l] != opt_1[pos - l]:
                    min_1 -= 1
                if s_new[pos - l] != opt_2[pos - l]:
                    min_2 -= 1
            if pos >= l - 1:
                min_flip = min(min_flip, min_1, min_2)
        return min_flip
        
        
        # n = len(s)
        # t = s + s
        # a = '01' * n
        # b = '10' * n
        # ans = n
        # da = 0
        # db = 0
        # for count in range(n * 2):
        #     if t[count] != a[count]:
        #         da += 1
        #     if t[count] != b[count]:
        #         db += 1
        #     if count >= n:
        #         if t[count - n] != a[count - n]:
        #             da -= 1
        #         if t[count - n] != b[count - n]:
        #             db -= 1
        #     if count >= n - 1:
        #         ans = min(ans, da, db)
        # return ans
        
        
        
#         #O(N^2) time and O(N) space - BRUTE FORCE
#         #shift 1 bit one at a time and then check the minimum # of type 2 actions necessary each time
#         opt_1 = ''.join(['0' if xx % 2 == 0 else '1' for xx in range(len(s))])
#         opt_2 = ''.join(['1' if xx % 2 == 0 else '0' for xx in range(len(s))])
        
#         def ret_minimum_type_2(s):
#             min_1 = min_2 = 0
#             for pos in range(len(s)):
#                 if s[pos] == opt_1[pos]:
#                     min_1 += 1
#                 if s[pos] == opt_2[pos]:
#                     min_2 += 1
#             return min(min_1, min_2)
        
#         dq = deque(s)
#         ret_min = len(s)
#         for count in range(len(s)):
#             ret_min = min(ret_min, ret_minimum_type_2(dq))
#             dq.rotate(1)
#             # dq.append(dq.popleft())
#         return ret_min
