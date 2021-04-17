class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
            
        
        
#         l_p,r_p = 0,0
#         sub_str = set()
#         max_len = 0
#         while r_p < len(s):
#             while s[r_p] in sub_str:
#                 sub_str.remove(s[l_p])
#                 l_p += 1
#             sub_str.add(s[r_p])
#             max_len = max(max_len, len(sub_str))
#             r_p += 1
        
#         return max_len