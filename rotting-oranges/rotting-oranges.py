class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #O(NM) time and O(NM) space
        #BFS
        dq = deque()
        x_len,y_len = len(grid[0]), len(grid)
        minutes = 0
        fresh_oranges = 0
        for yy in range(y_len):
            for xx in range(x_len):
                if grid[yy][xx] == 2:
                    dq.append([yy,xx,0])
                elif grid[yy][xx] == 1:
                    fresh_oranges += 1
                    
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        if dq:
            dq[-1][-1] = 1
        while dq:
            bad_og = dq.popleft()
            for dir_ in dirs:
                new_y, new_x = bad_og[0] + dir_[0], bad_og[1] + dir_[1]
                if 0 <= new_y < y_len and 0 <= new_x < x_len:
                    if grid[new_y][new_x] == 1:
                        dq.append([new_y, new_x, 0])
                        grid[new_y][new_x] = 2
                        fresh_oranges -= 1
            if bad_og[2] == 1 and dq:
                minutes += 1
                dq[-1][-1] = 1

        return minutes if fresh_oranges == 0 else -1
                

                    
                    
            