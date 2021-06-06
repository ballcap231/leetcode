class Solution:
    def minOperations(self, s: str) -> int:
        one_opt = []
        second_opt  = []
        for ii in range(len(s)):
            if ii % 2 == 0:
                one_opt.append('0')
                second_opt.append('1')
            else:
                one_opt.append('1')
                second_opt.append('0')
        
        move_one, move_second = 0,0
        for ii in range(len(s)):
            if s[ii] != one_opt[ii]:
                move_one += 1
            else:
                move_second += 1
        
        return min(move_one, move_second)