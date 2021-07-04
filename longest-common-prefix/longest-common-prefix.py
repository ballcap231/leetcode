class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #O(N) time where N == # chars in strs
        #O(1) space
        min_str = min(len(xx) for xx in strs)
        char_pos = 0
        if len(strs) == 1: return strs[0]
        
        while char_pos < min_str:
            for word_pos in range(1, len(strs)):
                first_word, second_word = strs[word_pos - 1], strs[word_pos]
                if first_word[char_pos] != second_word[char_pos]:
                    return strs[0][:char_pos]
            else:
                char_pos += 1
        
        return strs[0][:char_pos]