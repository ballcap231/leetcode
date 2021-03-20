class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        dir_pos = curr_x = curr_y = 0
        curr_dir = dirs[dir_pos]
        x_len,y_len = len(matrix), len(matrix[0])
        ans = []
        def valid_pos(xx, yy):
            if -1 < xx < x_len and -1 < yy < y_len and \
                matrix[xx][yy] is not None:
                return True
            return False
        
        while valid_pos(curr_x, curr_y):
            while valid_pos(curr_x, curr_y):
                ans.append(matrix[curr_x][curr_y])
                matrix[curr_x][curr_y] = None
                curr_x += curr_dir[0]
                curr_y += curr_dir[1]
            curr_x -= curr_dir[0]
            curr_y -= curr_dir[1]
            dir_pos = (dir_pos + 1) % 4
            curr_dir = dirs[dir_pos]
            curr_x += curr_dir[0]
            curr_y += curr_dir[1]
        return ans
        
        
        
        
        
        
        
        
#         dirs = [[0,1],[1,0],[0,-1],[-1,0]]
#         x_len,y_len = len(matrix), len(matrix[0])
#         pos = [0,0]
#         dir_pos = 0
#         curr_dir = dirs[dir_pos]
#         ret= []
        
#         def valid_pos(pos):
#             if -1 < pos[0] < x_len and -1 < pos[1] < y_len and \
#                 matrix[pos[0]][pos[1]] is not None:
#                 return True
#             return False
        
#         while valid_pos(pos):
#             while valid_pos(pos):
#                 ret.append(matrix[pos[0]][pos[1]])
#                 matrix[pos[0]][pos[1]] = None
#                 pos[0] += curr_dir[0]
#                 pos[1] += curr_dir[1]
#             pos[0] -= curr_dir[0]
#             pos[1] -= curr_dir[1]
#             dir_pos = (dir_pos + 1) % 4
#             curr_dir = dirs[dir_pos]
#             pos[0] += curr_dir[0]
#             pos[1] += curr_dir[1]
#         return ret
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         turn = [[0,1],[1,0],[0,-1],[-1,0]]
#         x_len = len(matrix)
#         y_len = len(matrix[0])
#         pos = [0,0]
#         curr_turn = 0
#         ans = []
#         move = turn[curr_turn]
#         def valid_pos(pos):
#             if pos[0] < 0 or pos[0] >= x_len or pos[1] < 0 or pos[1] >= y_len:
#                 return False
#             elif matrix[pos[0]][pos[1]] is None:
#                 return False
#             return True
        
#         while valid_pos(pos):
#             while valid_pos(pos):
#                 ans.append(matrix[pos[0]][pos[1]])
#                 matrix[pos[0]][pos[1]] = None
#                 pos[0] += move[0]
#                 pos[1] += move[1]
#             pos[0] -= move[0]
#             pos[1] -= move[1]
#             curr_turn = (curr_turn + 1) % 4
#             move = turn[curr_turn]
#             pos[0] += move[0]
#             pos[1] += move[1]
#         return ans
            