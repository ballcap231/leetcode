class Solution:
    def longestPalindrome(self, s: str) -> str:
        table = [[False for _ in range(len(s))] for _ in range(len(s))]
        max_length = 1
        start = len(s) - 1
        
        #Making all chars on diagonal to be True - 1 character alone is a palindrome
        for ii in range(len(s)):
            table[ii][ii] = True
        
        #Checking if all chars of len 2 are palindromes
        for ii in range(len(s) - 1):
            if s[ii] == s[ii + 1]:
                table[ii][ii + 1] = True
                if max_length == 1:
                    max_length = 2
                    start = ii
        
        
        for width in range(3, len(s) + 1):
            for i in range(len(s) - width + 1):
                j = i + width - 1
                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] = True
                    if width > max_length:
                        max_length = width
                        start = i
        
        return s[start:start + max_length]
        
        
        
        
        
        
        
#         if len(s) < 2:
#             return s
#         max_len = 1
#         start_p = 0
#         end_p = 0
#         def palindrome_calc(left_index, right_index):
#             while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
#                 left_index -= 1
#                 right_index += 1
#             return left_index + 1, right_index - 1
        
#         def check(index):
#             #return longest indices that result in a palindrome
#             max_l, max_r = index, index
#             #checking index 
#             L1_pc, R1_pc = palindrome_calc(index, index)
#             max_l,max_r = L1_pc, R1_pc
#             #checking index + 1
#             if s[index] == s[index + 1]:
#                 L2_pc, R2_pc = palindrome_calc(index, index+1)
#                 if R2_pc - L2_pc > R1_pc - L1_pc:
#                     max_l,max_r = L2_pc,R2_pc

#             return max_l,max_r
            

#         for index in range(len(s) - 1):
#             L, R = check(index)
            
#             if R - L + 1 > max_len:
#                 max_len = R - L + 1
#                 start_p = L
#                 end_p = R
                
            
#         return s[start_p:end_p + 1]