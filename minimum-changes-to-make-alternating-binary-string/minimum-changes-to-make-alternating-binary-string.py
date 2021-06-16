class Solution:
    def minOperations(self, s: str) -> int:
#         #O(N) time and O(N) space
#         one_opt = []
#         second_opt  = []
#         for ii in range(len(s)):
#             if ii % 2 == 0:
#                 one_opt.append('0')
#                 second_opt.append('1')
#             else:
#                 one_opt.append('1')
#                 second_opt.append('0')
        
#         move_one, move_second = 0,0
#         for ii in range(len(s)):
#             if s[ii] != one_opt[ii]:
#                 move_one += 1
#             else:
#                 move_second += 1
        
#         return min(move_one, move_second)



        n = len(s)
        t = s + s
        a = '01' * n
        b = '10' * n
        ans = n
        da = 0
        db = 0
        for count in range(n * 2):
            if t[count] != a[count]:
                da += 1
            if t[count] != b[count]:
                db += 1
            # if count >= n:
            #     if t[count - n] != a[count - n]:
            #         da -= 1
            #     if t[count - n] != b[count - n]:
            #         db -= 1
            if count >= n - 1:
                ans = min(ans, da, db)
                return ans
        return ans