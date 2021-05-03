class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #O(N * M) time and O(min(M + N)) space
        x_len = len(grid)
        y_len = len(grid[0])
        
        self.max_area = 0
        def is_valid_loc(xx,yy):
            if xx < 0 or xx >= x_len or yy < 0 or yy >= y_len\
                or not grid[xx][yy]:
                return False
            return True
        
        def BFS(xx,yy):
            dq = deque()
            dq.append((xx,yy))
            curr_area = 0
            while dq:
                curr_x, curr_y = dq.popleft()
                if grid[curr_x][curr_y]:
                    curr_area += 1
                    self.max_area = max(self.max_area, curr_area)
                    grid[curr_x][curr_y] = 0
                    for dir_x, dir_y in [(-1,0),(1,0), (0,1), (0,-1)]:
                        new_x, new_y = curr_x + dir_x, curr_y + dir_y
                        if is_valid_loc(new_x, new_y):
                            dq.append((new_x, new_y))
                
        for xx in range(x_len):
            for yy in range(y_len):
                if grid[xx][yy]:
                    BFS(xx,yy)
        
        return self.max_area
            
        
        
        
        
        
        
        
# class Solution:
#     directions = [              
#         [-1, 0],
#         [0, 1],
#         [1, 0],
#         [0, -1]
#     ]
    
#     def maxAreaSingleIsland(self, grid, curr_row, curr_col, count):
#         if curr_row < 0 or curr_col < 0 or curr_row >= len(grid) or curr_col >= len(grid[0]):
#             return 0
#         if grid[curr_row][curr_col] == 1:
#             grid[curr_row][curr_col] = 0
#             count += 1
#             for direct in self.directions:
#                 row = direct[0] + curr_row
#                 col = direct[1] + curr_col
#                 return count + self.maxAreaSingleIsland(grid, row, col, count)
#         else:
#             return count
        
#     """
#     [[1,1,0,0,0],
#      [1,1,0,0,0],
#      [0,0,0,1,1],
#      [0,0,0,1,1]]
#     """
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         max_area = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     max_area = max(max_area, self.maxAreaSingleIsland(grid, i, j, 0))
#         return max_area