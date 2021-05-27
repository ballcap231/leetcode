class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #O(N^3 + |wordDict|) time and O(N + |wordDict|) space
        words = set(wordDict)
        is_word = [0 for _ in range(len(s) + 1)]
        is_word[0] = 1 #empty string is a valid word
        
        for right in range(1, len(s) + 1):
            for left in range(right):
                if is_word[left] and s[left:right] in words:
                    is_word[right] = 1
                    break
        return is_word[-1]
        
        
        
        
#         #Brute force using Backtracking
#         #Worst case example: s = 'aaaaab' and wordDict = {'a','aa','aaa','aaaa'}
#         #O(2^N) time and O(N + |wordDict|) space complexity
#         len_word = len(s)
#         dictionary = set(wordDict)

#         def check_substring(start):
#             if start == len_word:
#                 return True
#             for curr_pos in range(start + 1, len_word + 1):
#                 #O(N) operation to slice string
#                 if s[start:curr_pos] in dictionary and check_substring(curr_pos):
#                     return True
#             return False
        
#         return check_substring(0)
        
        
        
        
#         #Worst case example: s = 'aaaaab' and wordDict = {'a','aa','aaa','aaaa'}
#         #O(N^3 + |wordDict|) time and O(N + |wordDict|) space complexity
#         len_word = len(s)
#         dictionary = set(wordDict)

#         @lru_cache(maxsize=None)#O(N^2) operation to check all combinations of substrings
#         def check_substring(start):
#             if start == len_word:
#                 return True
#             for curr_pos in range(start + 1, len_word + 1):
#                 #O(N) operation to slice string
#                 if s[start:curr_pos] in dictionary and check_substring(curr_pos):
#                     return True
#             return False
        
#         return check_substring(0)



#O(N^2 + MK) time and O(N + MK) space
# "Assuming the dictionary of words to be K with average length of M the time and space complexity would be O(MK)"
#https://leetcode.com/problems/word-break/discuss/729064/Python-or-DP-%2B-Trie-or-O(N2)-O(N)
# class Node:
#     def __init__(self):
#         self.children = dict()
#         self.is_word = False
# class Trie:
#     def __init__(self):
#         self.root = Node()
#     def add_word(self, word):
#         node = self.root
#         for char in word:
#             node = node.children.setdefault(char, Node())
#         node.is_word = True
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         trie = Trie()
#         for word in wordDict:
#             trie.add_word(word)
#         @lru_cache(maxsize=None)
#         def valid_substr(start):
#             if start >= len(s):
#                 return True
#             node = trie.root
#             for pos in range(start, len(s)):
#                 if s[pos] not in node.children:
#                     return False
#                 node = node.children[s[pos]]
#                 if node.is_word and valid_substr(pos + 1):
#                     return True
#         return valid_substr(0)
                
                
            
            
            