class Solution:
    def is_valid_pos(self, xx, yy):
        if -1 < xx < self.x_len and -1 < yy < self.y_len:
            return True
        return False
    
    def dfs(self,xx,yy):
        if self.is_valid_pos(xx,yy) and self.board[xx][yy] == 'O':
            self.board[xx][yy] = 'Z'
            self.dfs(xx + 1, yy)
            self.dfs(xx - 1, yy)
            self.dfs(xx, yy + 1)
            self.dfs(xx, yy - 1)
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #O(N * M ) time and O(N * M) space
        self.board = board
        self.x_len, self.y_len = len(self.board), len(self.board[0])
        if self.x_len < 3 or self.y_len < 3:
            return
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        curr_x = curr_y = 0
        for direction in dirs:
            while self.is_valid_pos(direction[0] + curr_x, direction[1] + curr_y):
                curr_x += direction[0]
                curr_y += direction[1]
                self.dfs(curr_x, curr_y)
        
        for xx in range(1, self.x_len - 1):
            for yy in range(1, self.y_len - 1):
                if self.board[xx][yy] == 'O':
                    self.board[xx][yy] = 'X'
        
        for xx in range(self.x_len):
            for yy in range(self.y_len):
                if self.board[xx][yy] == 'Z':
                    self.board[xx][yy] = 'O'
                    
                    
                    
        