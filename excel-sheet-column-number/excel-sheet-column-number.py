class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #O(N) time and (1) space
        # ABA
        # 1 x 26 ^ 2 + 2 x 26 ^ 1  + 1 x 26 ^ 0
        ret_num = 0
        letters = string.ascii_uppercase
        letters_map = {char:pos + 1 for pos, char in enumerate(letters)}
        for pos in range(len(columnTitle) - 1, -1, -1):
            ret_num += letters_map[columnTitle[pos]] *  26 ** (len(columnTitle) - pos - 1) 
        return ret_num