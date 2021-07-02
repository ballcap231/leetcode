class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x_flag = y_flag = False
        if matrix[0][0] == 0:
            x_flag = y_flag = True
        x_len, y_len = len(matrix), len(matrix[0])
        
        for xx in range(1, x_len):
            for yy in range(1, y_len):
                if matrix[xx][yy] == 0:
                    matrix[0][yy] = "X" if matrix[0][yy] != 0 else 0
                    matrix[xx][0] = "X" if matrix[xx][0] != 0 else 0
        
        for xx in range(1, x_len):
            if matrix[xx][0] in ("X", 0):
                for yy in range(1, y_len):
                    matrix[xx][yy] = 0
            if matrix[xx][0] == 0:
                x_flag = True
        
        for yy in range(1, y_len):
            if matrix[0][yy] in ("X", 0):
                for xx in range(1, x_len):
                    matrix[xx][yy] = 0
            if matrix[0][yy] == 0:
                y_flag = True
        
        for xx in reversed(range(x_len)):
            if matrix[xx][0] == 0:
                x_flag = True
            elif x_flag or matrix[xx][0] == "X":
                matrix[xx][0] = 0
        
        for yy in reversed(range(y_len)):
            if matrix[0][yy] == 0:
                y_flag = True
            elif y_flag or matrix[0][yy] == "X":
                matrix[0][yy] = 0
        
        
        
        
        
        
        
#         x_flag = False
#         y_flag = False
#         for xx in range(len(matrix)):
#             for yy in range(len(matrix[0])):
#                 if xx == 0:
#                     if matrix[xx][yy] == 0:
#                         y_flag = True
#                 elif yy == 0:
#                     if matrix[xx][yy] == 0:
#                         x_flag = True
#                 elif matrix[xx][yy] == 0:
#                     matrix[xx][0] = 0
#                     matrix[0][yy] = 0

#         for xx in range(1,len(matrix)):
#             if matrix[xx][0] == 0:
#                 for yy in range(1,len(matrix[0])):
#                         matrix[xx][yy] = 0
                        
#         for yy in range(1,len(matrix[0])):
#             if matrix[0][yy] == 0:
#                 for xx in range(1,len(matrix)):
#                         matrix[xx][yy] = 0
                        
#         if matrix[0][0] == 0:
#             for xx in range(1,len(matrix)):
#                 matrix[xx][0] = 0
#             for yy in range(1,len(matrix[0])):
#                 matrix[0][yy] = 0
#         else:
#             if x_flag:
#                 for xx in range(len(matrix)):
#                     matrix[xx][0] = 0
#             if y_flag:
#                 for yy in range(len(matrix[0])):
#                     matrix[0][yy] = 0
                