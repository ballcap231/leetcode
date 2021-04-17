class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s): return 0
        char_counts = Counter(s)
        max_unique = len(char_counts)
        longest_str = 0
        
        for unique_count in range(1,max_unique + 1):
            L,R = -1,0
            curr_char_counts = Counter()
            while R < len(s):
                curr_char_counts[s[R]] += 1 
                while len(curr_char_counts) > unique_count:
                    L += 1
                    curr_char_counts[s[L]] -= 1
                    if curr_char_counts[s[L]] == 0:
                        curr_char_counts.pop(s[L])
                if all(xx >= k for xx in curr_char_counts.values()):
                    longest_str = max(longest_str, R - L)
                
                
                
                R += 1
        
        return longest_str
                       
        
        
        
        
#         if k > len(s): return 0
#         counts = Counter(s)
        
#         longest_str = 0
        
#         curr_counts = Counter()
#         left = -1
        
#         for right in range(len(s)):
#             if counts[s[right]] < k:
#                 curr_counts = Counter() 
#                 left = right
#             else:
#                 curr_counts[s[right]] += 1
#                 for num_strs in curr_counts.values():
#                     if num_strs < k:
#                         break
#                 else:
#                     longest_str = max(longest_str, right - left)
#         return longest_str
            
        
        