class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        #Binary search soln
        
        max_repeat = len(sequence) // len(word)
        L,R = 0, max_repeat
        
        while L < R:
            M = (L + R) // 2
            
            if word * M in sequence:
                if word * (M + 1) not in sequence:
                    return M
                L = M + 1
            else:
                R = M
        return L
            
        
        
        
        
        
        
# #         #KMP algorithm - O(N) time and O(N) space where N is length of sequence
# #         #KMP is used to search for a substring (W), in a given string (S), in O(m+n) 
# #         #or O(m) time since the given string (S) should be greater than the substring 
#         if len(sequence) < len(word): return 0
#         #creating string with maximum number of k reptitions possible
#         max_repeat = len(sequence) // len(word)
#         max_repeat_str = word * max_repeat

#         #creating prefix-suffix partial match table
#         match_table = self.create_partial_match_table(max_repeat_str)
#         seq_pointer = word_pointer = curr_max_repeat = 0
#         while seq_pointer < len(sequence):
#             #check if current chars match - move forward if so
#             if sequence[seq_pointer] == max_repeat_str[word_pointer]:
#                 seq_pointer += 1
#                 word_pointer += 1
#                 #log max_repeating, if it matches maximum possible, return early
#                 curr_max_repeat = max(curr_max_repeat, word_pointer // len(word))
#                 if curr_max_repeat == max_repeat: return curr_max_repeat
#             else:
#                 #if current chars don't match - only 2 possible steps:
#                 #1.move seq_pointer forward - only do so if word_pointer points to first char
#                 #2.don't move seq_pointer forward and move word_pointer to next matching prefix/suffix
#                 if word_pointer == 0:
#                     seq_pointer += 1
#                 else:
#                     word_pointer = match_table[word_pointer - 1]    
#         return curr_max_repeat
#     def create_partial_match_table(self, string):
#         match_table = [0]
#         for char in string[1:]:
#             if char == string[match_table[-1]]:
#                 match_table.append(match_table[-1] + 1)
#             else:
#                 match_table.append(0)
#         return match_table
    
#         #Brute Force
#         #O(N^2) time and O(N) space where N is the length of sequence
#         count = 1
#         max_count = 0
#         max_repeat = len(sequence) // len(word)
        
#         while word * count in sequence:
#             max_count += 1
#             count += 1
        
#         return max_count
        