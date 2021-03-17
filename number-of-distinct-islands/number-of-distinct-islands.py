class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        x_len,y_len = len(grid), len(grid[0])
        def check_bounds(xx,yy):
            if -1 < xx < x_len and -1 < yy < y_len:
                return True
            return False
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        
        def bfs(xx,yy):
            deq = deque()
            deq.append((xx,yy))
            land = []
            while deq:
                pos_x, pos_y = deq.popleft()
                for x_dir, y_dir in dirs:
                    new_x, new_y = pos_x + x_dir, pos_y + y_dir
                    if not check_bounds(new_x, new_y) or not grid[new_x][new_y]:
                        continue
                    deq.append((new_x,new_y))
                    grid[new_x][new_y] = 0
                    land.append((new_x - xx, new_y - yy))
            islands.add(tuple(land))
                    
        for xx in range(x_len):
            for yy in range(y_len):
                if grid[xx][yy]:
                    bfs(xx,yy)
                
        return len(islands)