class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if not A: return  True
        
        def create_partial_match_table(substring):
          #creates indices array of partial match table
          #(aka longest common prefix-suffix array since the indices values indicates there is the same prefix and suffix)
            match_table = [0]

            for curr_pos in range(1, len(substring)):
                match_index = match_table[-1]
                #visit backwards repeatedly until we find a valid prefix-suffix combination
                while match_index > 0 and substring[match_index] != substring[curr_pos]:
                    match_index = match_table[match_index - 1]
                match_table.append(match_index + 1 if substring[match_index] == substring[curr_pos] else match_index)
            return match_table
        
        
        def KMP(string, substring):


            partial_match_table = create_partial_match_table(substring)
            string_pointer = substring_pointer = 0

            while string_pointer < len(string):
                if string[string_pointer] == substring[substring_pointer]:
                    string_pointer += 1
                    substring_pointer += 1
                    if substring_pointer == len(substring):
                        return True
                else:
                    string_pointer += 1 if substring_pointer == 0 else 0
                    substring_pointer = 0 if substring_pointer == 0 else partial_match_table[substring_pointer - 1]

            return False
        
        
        
        return KMP(A * 2, B)
            