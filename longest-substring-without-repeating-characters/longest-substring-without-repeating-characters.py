class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #O(N) time and O(1) space
        L = R = 0
        max_len = 0
        chars = set()
        while R < len(s):
            curr_char = s[R]
            while curr_char in chars:
                chars.discard(s[L])
                L += 1
            R += 1
            chars.add(curr_char)
            max_len = max(max_len, R - L)
        return max_len