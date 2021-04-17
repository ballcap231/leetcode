class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        #O(N) time and O(1) space
        max_len = 0
        L = R = 0
        chars = Counter()
        while R < len(s):
            char = s[R]
            while len(chars) >= 2 and char not in chars:
                chars[s[L]] -= 1
                if chars[s[L]] == 0:
                    chars.pop(s[L])
                L += 1
            R += 1
            chars[char] += 1
            max_len = max(max_len, R - L)
        return max_len    
            
            