class Node:
    def __init__(self):
        self.children = dict()
        self.is_word = False
class Trie:
    def __init__(self):
        self.root = Node()
    def add_word(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, Node())
        node.is_word = True
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.add_word(word)
        @lru_cache(maxsize=None)
        def valid_substr(start):
            if start >= len(s):
                return True
            node = trie.root
            for pos in range(start, len(s)):
                if s[pos] not in node.children:
                    return False
                node = node.children[s[pos]]
                if node.is_word and valid_substr(pos + 1):
                    return True
        return valid_substr(0)
                
                
            
            
            