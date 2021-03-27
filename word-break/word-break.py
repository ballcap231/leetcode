class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_word = len(s)
        dictionary = set(wordDict)

        @lru_cache(maxsize=None)
        def check_substring(start):
            if start == len_word:
                return True
            for curr_pos in range(start + 1, len_word + 1):
                if s[start:curr_pos] in dictionary and check_substring(curr_pos):
                    return True
            return False
        
        return check_substring(0)




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
                
                
            
            
            