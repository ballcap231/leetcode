import string
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #O(N ^ (1/26)) time and O(1) space
        chars = string.ascii_uppercase
        new_str = deque()
        while columnNumber:
            new_str.appendleft(chars[(columnNumber - 1) % 26])
            columnNumber = (columnNumber - 1) // 26
        return ''.join(list(new_str))
        