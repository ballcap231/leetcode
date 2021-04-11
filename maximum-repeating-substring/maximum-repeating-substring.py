class Solution:
    def create_partial_match_table(self, string):
        match_table = [0]

        for char in string[1:]:
            if char == string[match_table[-1]]:
                match_table.append(match_table[-1] + 1)
            else:
                match_table.append(0)
        return match_table
    
    def maxRepeating(self, sequence: str, word: str) -> int:
        #O(N) time and O(N) space where N is length of sequence
        if len(sequence) < len(word): return 0
        max_repeat = len(sequence) // len(word)
        max_repeat_str = word * max_repeat

        
        match_table = self.create_partial_match_table(max_repeat_str)
        seq_pointer = word_pointer = curr_max_repeat = 0
        
        while seq_pointer < len(sequence):
            if sequence[seq_pointer] == max_repeat_str[word_pointer]:
                seq_pointer += 1
                word_pointer += 1
                curr_max_repeat = max(curr_max_repeat, word_pointer // len(word))
                if curr_max_repeat == max_repeat: return curr_max_repeat
            else:
                if word_pointer == 0:
                    seq_pointer += 1
                else:
                    word_pointer = match_table[word_pointer - 1]        
        
        return curr_max_repeat
        

#         #Brute Force
#         #O(N^2) time and O(N) space where N is the length of sequence
#         count = 1
#         max_count = 0
#         max_repeat = len(sequence) // len(word)
        
#         while word * count in sequence:
#             max_count += 1
#             count += 1
        
#         return max_count
        