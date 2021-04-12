class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        KMP algorithm
        time-space complexity: O(n), O(n)
        """
#         rev = s[::-1]
        
#         new_s =  s + "#" + rev
        
#         match_table = [0 for xx in range(len(new_s))]
        
#         for curr_pos in range(1, len(new_s)):
#             prefix_boundary = match_table[curr_pos - 1]
            
#             while prefix_boundary > 0 and new_s[curr_pos] != new_s[prefix_boundary]:
#                 prefix_boundary = match_table[prefix_boundary - 1]
            
#             if new_s[prefix_boundary] == new_s[curr_pos]:
#                 match_table[curr_pos] = prefix_boundary + 1
        
#         return new_s[0: len(s) - match_table[len(new_s) - 1]] + s

        
        
        rev = s[::-1]
        
        new_s =  s + "#" + rev
        def create_partial_match_table(pattern):
            """ Calculate partial match table: String -> [Int]"""
            ret = [0]

            for i in range(1, len(pattern)):
                j = ret[i - 1]
                while j > 0 and pattern[j] != pattern[i]:
                    j = ret[j - 1]
                ret.append(j + 1 if pattern[j] == pattern[i] else j)
            return ret
        
        table = create_partial_match_table(new_s)
        matches = table[-1]
        print(rev[:len(rev) - matches])
        print(new_s)
        print(table)
        return rev[:len(rev) - matches] + s
        
        
#         if s=="": return s #basecase

#         pattern = s + s[::-1]
        
#         prefix = [-1] * len(pattern)
#         j = -1
#         for i in range(1, len(pattern)):
#             while j>-1 and pattern[j+1]!=pattern[i]:
#                 j = prefix[j]
#             j += 1
#             prefix[i] = j
#         print(prefix, len(prefix), len(s))
#         i = prefix[-1]
#         while i >= len(s):
#             i = prefix[i]
#         return s[i+1:][::-1] + s
        
        
        
        
        
        
        
        
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
        
        