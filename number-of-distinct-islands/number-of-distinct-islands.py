class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        #O(M*N) time and O(M * N) space since we are storing distinct islands
        islands = set()
        x_len,y_len = len(grid), len(grid[0])
        def check_bounds(xx,yy):
            if -1 < xx < x_len and -1 < yy < y_len and grid[xx][yy]:
                return True
            return False
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        #BFS SOLUTION
        
        # def bfs(xx,yy):
        #     deq = deque()
        #     deq.append((xx,yy))
        #     land = []
        #     while deq:
        #         pos_x, pos_y = deq.popleft()
        #         for x_dir, y_dir in dirs:
        #             new_x, new_y = pos_x + x_dir, pos_y + y_dir
        #             if not check_bounds(new_x, new_y):
        #                 continue
        #             deq.append((new_x,new_y))
        #             grid[new_x][new_y] = 0
        #             land.append((new_x - xx, new_y - yy))
        #     islands.add(tuple(land))

        # for xx in range(x_len):
        #     for yy in range(y_len):
        #         if grid[xx][yy]:
        #             bfs(xx,yy)
        
        # return len(islands)
        
        #DFS SOLUTION
        
        def dfs(xx,yy):
            if not check_bounds(xx,yy):
                return
            grid[xx][yy] = 0
            self.island.append((xx - self.first_x, yy - self.first_y))
            dfs(xx - 1, yy)
            dfs(xx + 1, yy)
            dfs(xx, yy - 1)
            dfs(xx, yy + 1)
            
        for xx in range(x_len):
            for yy in range(y_len):
                if grid[xx][yy]:
                    self.island = []
                    self.first_x, self.first_y = xx,yy
                    dfs(xx,yy)
                    islands.add(tuple(self.island))

        return len(islands)