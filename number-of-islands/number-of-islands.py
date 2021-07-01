from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #BFS solution
        #O(M X N) time for M rows and N columns
        #O(min(M,N)) space complexity
        
        #Space complextiy explanation: https://imgur.com/gallery/M58OKvB
        if not grid:
            return 0
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        def check_in_bound(row,col):
            if row > rows - 1 or row < 0 or col < 0 or col > cols - 1:
                return False
            return True
        def bfs(row,col):
            self.queue.append([row,col])
            while self.queue:
                row,col = self.queue.popleft()
                #out of bounds and bfs only if it is land
                if check_in_bound(row,col) \
                and grid[row][col] == "1":
                    grid[row][col] = "0"
                    self.queue.append([row-1,col])
                    self.queue.append([row+1,col])
                    self.queue.append([row,col-1])
                    self.queue.append([row,col+1])

        for row, yy in enumerate(grid):
            for col, xx in enumerate(yy):
                if xx == "1" and (row,col):
                    islands += 1
                    self.queue = deque()
                    bfs(row,col)
                    
        return islands
                    
                    
                
        