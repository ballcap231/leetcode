class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 1
        max_count = 0
        max_repeat = len(sequence) // len(word)
        
        while word * count in sequence:
            max_count += 1
            count += 1
        
        return max_count
        
#         max_repeat = len(sequence) // len(word)
#         max_repeat_str = word * (max_repeat)
#         def make_LCP_indices(string):
#             LCP_indices = [0]
            
#             for char in string[1:]:
#                 if char == LCP_indices[-1]:
#                     LCP_indices.append(LCP_indices[-1] + 1)
#                 else:
#                     LCP_indices.append(0)
#             return LCP_indices
        
#         LCP_indices = make_LCP_indices(max_repeat_str)
        
        
        
        
        
        
        
        
        
        
#         s, w = len(sequence), len(word)
#         max_repeat = s // w
#         failure = [0] * (w * max_repeat + 1)
#         repeat_words = word * max_repeat + '$'
#         result = 0

#         j = 0
#         for i in range(1, len(repeat_words)):
#             while j > 0 and repeat_words[j] != repeat_words[i]:
#                 j = failure[j-1]
#             j += repeat_words[j] == repeat_words[i]
#             failure[i] = j

#         j = 0
#         for i, c in enumerate(sequence):
#             while j > 0 and repeat_words[j] != c:
#                 j = failure[j-1]
#             j += repeat_words[j] == c
#             result = max(result, j // w)

#         return result
        
        
        