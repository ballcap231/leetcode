
class Solution:
    def reset(self):
        while self.popped:
            self.table.add(self.popped.pop())
    def check_square(self, x_pos, y_pos):
        for xx in range(x_pos, x_pos + 3):
            for yy in range(y_pos, y_pos + 3):
                if not self.check_value(self.board[xx][yy]):
                    return False
        return True
    def check_value(self, val):
        if val != '.':
            if val not in self.table:
                return False
            self.table.remove(val)
            self.popped.append(val)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #O(N^2) time and O(N) space where N = 9 in this case
        self.board = board
        self.table = set([str(xx) for xx in range(1, 10)])
        self.popped = []
        
        for xx in range(9):
            for yy in range(9):
                if not self.check_value(self.board[xx][yy]):
                    return False
            self.reset()

        for xx in range(9):
            for yy in range(9):
                if not self.check_value(self.board[yy][xx]):
                    return False
            self.reset()
        
        for xx in range(0, 9, 3):
            for yy in range(0, 9, 3):
                if not self.check_square(xx, yy):
                    return False
                self.reset()
        return True
        
    
