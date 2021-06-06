class Solution:
    def longestPalindrome(self, s: str) -> str:
#         #Bottom-Up DP - using 2-D matrix for 1-D String
#         #O(N^2) time and space
        
#         #Boolean matrix of palindromes
#         table = [[False for _ in range(len(s))] for _ in range(len(s))]
        
#         max_length = 0
#         start = end = 0
        
#         #Filling in bottom left triangle of square boolean palindrome matrix
#         #row value represents position of end of string 
#         #col value represents position of start of string 
#         for row in range(len(s)):
#             for col in range(row + 1):
#                 #Single char is always palindrome
#                 if row == col:
#                     table[row][col] = True
#                 #2 chars are palindromes if they are equal
#                 elif row == col + 1:
#                     table[row][col] = s[row] == s[col]
#                 #3 chars or more are palindromes if the first & last chars are equal and if inner substring are palindromes
#                 else:
#                     table[row][col] = (s[row] == s[col] and table[row - 1][col + 1])
#                 #if this position is a palindrome, update max palindrome length string positions
#                 if table[row][col] and row - col + 1 > max_length:
#                     max_length = row - col + 1
#                     start = col
#                     end = row
                    
#         return s[start:end + 1]
                    
        
        if len(s) < 2:
            return s
        max_len = 1
        start_p = 0
        end_p = 0
        def palindrome_calc(left_index, right_index):
            while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
                left_index -= 1
                right_index += 1
            return left_index + 1, right_index - 1
        
        def check(index):
            #return longest indices that result in a palindrome
            max_l, max_r = index, index
            #checking index 
            L1_pc, R1_pc = palindrome_calc(index, index)
            max_l,max_r = L1_pc, R1_pc
            #checking index + 1
            if s[index] == s[index + 1]:
                L2_pc, R2_pc = palindrome_calc(index, index+1)
                if R2_pc - L2_pc > R1_pc - L1_pc:
                    max_l,max_r = L2_pc,R2_pc

            return max_l,max_r
            

        for index in range(len(s) - 1):
            L, R = check(index)
            
            if R - L + 1 > max_len:
                max_len = R - L + 1
                start_p = L
                end_p = R
                
            
        return s[start_p:end_p + 1]