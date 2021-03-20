class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #O(N^2) time and O(1) space
        arr = [[0 for _ in range(n)] for _ in range(n) ]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        curr_x = curr_y = dir_pos = 0
        fill_num = 1
        curr_dir = dirs[dir_pos]
        
        def valid_pos(xx,yy):
            if -1 < xx < n and -1 < yy < n and \
                not arr[xx][yy]:
                return True
            return False
        
        while valid_pos(curr_x,curr_y):
            while valid_pos(curr_x, curr_y):
                arr[curr_x][curr_y] = fill_num
                fill_num += 1
                curr_x += curr_dir[0]
                curr_y += curr_dir[1]
            curr_x -= curr_dir[0]
            curr_y -= curr_dir[1]
            dir_pos = (dir_pos + 1) % 4
            curr_dir = dirs[dir_pos]
            curr_x += curr_dir[0]
            curr_y += curr_dir[1]
        return arr
                
                
        