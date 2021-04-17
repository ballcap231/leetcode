from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        max_len = 0

        for most_dist in (1,2):
            L = R = 0
            chars = Counter()
            while R < len(s):
                char = s[R]
                while len(chars) >= most_dist and char not in chars:
                    chars[s[L]] -= 1
                    if chars[s[L]] == 0:
                        chars.pop(s[L])
                    L += 1
                R += 1
                chars[char] += 1
                max_len = max(max_len, R - L)
        return max_len    
        
        # if len(s) < 2:
        #     return len(s)
        # counter = collections.defaultdict(int)
        # left = 0
        # for right in range(len(s)):
        #     counter[s[right]] += 1
        #     if len(counter) > 2:
        #         counter[s[left]] -= 1
        #         if not counter[s[left]]:
        #             counter.pop(s[left])
        #         left += 1
        # return right - left + 1
            
            