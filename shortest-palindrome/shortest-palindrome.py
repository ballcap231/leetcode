class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        KMP algorithm
        time-space complexity: O(n), O(n)
        """
        if s=="": return s #basecase

        pattern = s + s[::-1]
        
        prefix = [-1] * len(pattern)
        j = -1
        for i in range(1, len(pattern)):
            while j>-1 and pattern[j+1]!=pattern[i]:
                j = prefix[j]
            j += 1
            prefix[i] = j

        i = prefix[-1]
        while i >= len(s):
            i = prefix[i]
        return s[i+1:][::-1] + s
        
        
        
        
        
        
        
        
#         #Brute force - O(N^2) time and O(N) space
#         s_arr = list(s)
#         def is_palindrome(string:list):
#             for l in range(len(string) // 2):
#                 if string[l] != string[len(string) - l - 1]:
#                     return False
#             return True
        
#         palindrome_range = 0
#         #Finding the largest palindrome string starting from the end
#         for curr_pos in range(len(s_arr),0,-1):
#             if is_palindrome(s_arr[:curr_pos]):
#                 palindrome_range = curr_pos - 1
#                 break
        
#         prefix_str = []
        
#         for pos in range(len(s_arr) - 1, palindrome_range, -1):
#             prefix_str.append(s_arr[pos])
        
#         return ''.join(prefix_str + s_arr)
        
        