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
        #O(N * M  * 3^K + P) time
        #O(P) space
        # N and M are length of width of board, K is max length of all strings in words, P is number of chars in words list
        trie = Trie()
        for word in words:
            trie.add_word(word)
        self.found_words = []
        x_len, y_len = len(board), len(board[0])
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        def backtrack(xx, yy, parent_node):
            if 0 > xx or xx >= x_len or 0 > yy or yy >= y_len or \
                board[xx][yy] not in parent_node.children:
                return
            curr_char = board[xx][yy]
            child_node = parent_node.children[curr_char]
            if child_node.is_word:
                self.found_words.append(child_node.final_word)
                #Removing word from leaf node after being recorded
                child_node.is_word = False
                child_node.final_word = None

            board[xx][yy] = '#'
            for move in moves:
                new_x, new_y = xx + move[0], yy + move[1]
                backtrack(new_x, new_y, child_node)
            board[xx][yy] = curr_char
            #Pruning node if it is not a word and doesn't have children
            if not child_node.is_word and not child_node.children:
                parent_node.children.pop(curr_char)
            
        for x_pos in range(x_len):
            for y_pos in range(y_len):
                backtrack(x_pos, y_pos, trie.root)
        return self.found_words
                
            
            