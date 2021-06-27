class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        #O((R * C)^2) time and O(1) space
        rows, cols = len(board), len(board[0])
        crushed = False
        #flag horizontal
        for R in range(rows):
            for C in range(2, cols):
                if abs(board[R][C]) == abs(board[R][C - 1]) == abs(board[R][C - 2]) != 0:
                    board[R][C] = board[R][C - 1] = board[R][C - 2] = -abs(board[R][C])
                    crushed = True
        #flag vertical
        for C in range(cols):
            for R in range(2, rows):
                if abs(board[R][C]) == abs(board[R - 1][C]) == abs(board[R - 2][C]) != 0:
                    board[R][C] = board[R - 1][C] = board[R - 2][C] = -abs(board[R][C])
                    crushed = True
        
        #shifting all candy down the board'
        #Uses 2 loop approach from https://leetcode.com/problems/move-zeroes/solution/
        for col in range(cols):
            bottom = rows - 1
            #Shifting all cells > 0 down 
            for top in reversed(range(rows)):
                if board[top][col] > 0:
                    board[bottom][col] = board[top][col]
                    bottom -= 1
            # Setting leftover cells to be 0    
            for new_bottom in range(bottom, -1, -1):
                board[new_bottom][col] = 0
                
        return self.candyCrush(board) if crushed else board
        

        
        
        