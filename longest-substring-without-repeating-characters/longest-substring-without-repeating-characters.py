class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        curr_char = set()
        max_len = curr_len = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in curr_char:
                curr_char.remove(s[l])
                curr_len -= 1
                l += 1
            curr_char.add(s[r])
            curr_len += 1
            max_len = max(max_len, curr_len)
        return max_len
        
        
        
        # #O(N) time and O(1) space
        # L = R = 0
        # max_len = 0
        # chars = set()
        # while R < len(s):
        #     curr_char = s[R]
        #     while curr_char in chars:
        #         chars.discard(s[L])
        #         L += 1
        #     R += 1
        #     chars.add(curr_char)
        #     max_len = max(max_len, R - L)
        # return max_len