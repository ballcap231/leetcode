class Node:
    def __init__(self, is_word = False):
        self.children = {}
        self.is_word = is_word
        self.final_word = None
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_word = True
        node.final_word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)
        self.found_words = set()
        x_len, y_len = len(board), len(board[0])
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        def backtrack(xx, yy, node):
            if 0 > xx or xx >= x_len or 0 > yy or yy >= y_len or \
                board[xx][yy] not in node.children:
                return
            curr_char = board[xx][yy]
            new_node = node.children[curr_char]
            if new_node.is_word:
                self.found_words.add(new_node.final_word)
            
            board[xx][yy] = '#'
            for move in moves:
                new_x, new_y = xx + move[0], yy + move[1]
                backtrack(new_x, new_y, new_node)
            board[xx][yy] = curr_char
            return
        for x_pos in range(x_len):
            for y_pos in range(y_len):
                backtrack(x_pos, y_pos, trie.root)
        return list(self.found_words)
                
            
            