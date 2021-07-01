class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x_len = len(board)
        y_len = len(board[0])
        
        def backtrack(xx, yy, word_pos):
            if 0 > xx or xx >= x_len or 0 > yy or yy >= y_len or board[xx][yy] == 0:
                return False
            if board[xx][yy] == word[word_pos]:
                if word_pos == len(word) - 1:
                    return True
                
                old_char = board[xx][yy]
                board[xx][yy] = 0
                
                new_pos = word_pos + 1
                if backtrack(xx + 1, yy, new_pos) or backtrack(xx - 1, yy, new_pos) \
                    or backtrack(xx, yy + 1, new_pos) or backtrack(xx, yy - 1, new_pos):
                    return True
                
                board[xx][yy] = old_char
            return False
        
        for x_pos in range(x_len):
            for y_pos in range(y_len):
                if backtrack(x_pos, y_pos, 0):
                    return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
#         self.board = board
#         self.x_len = len(board)
#         self.y_len = len(board[0])
#         def backtrack(xx,yy, substring):
#             if not substring or xx < 0 or yy < 0 or xx >= self.x_len or yy >= self.y_len \
#                     or self.board[xx][yy] != substring[0]:
#                 return False
#             elif self.board[xx][yy] == substring:
#                 return True
#             self.board[xx][yy] = '#'
#             for x_turn,y_turn in [(-1,0),(1,0),(0,-1),(0,1)]:
#                 ret = backtrack(xx + x_turn, yy + y_turn, substring[1:])
#                 if ret:
#                     break
#             self.board[xx][yy] = substring[0]
#             return ret
        
#         for xx in range(self.x_len):
#             for yy in range(self.y_len):
#                 if backtrack(xx,yy,word):
#                     return True

#         return False
                
        
            