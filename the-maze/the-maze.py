class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        x_len, y_len = len(maze), len(maze[0])
        dest_tuple = tuple(destination)
        def get_next_pos(xx, yy, move):
            next_x, next_y = xx + move[0], yy + move[1]
            while 0 <= next_x < x_len and 0 <= next_y < y_len and \
                maze[next_x][next_y] != 1:
                xx = next_x
                yy = next_y
                next_x += move[0]
                next_y += move[1]
            return (xx, yy)
        
        
        
        dq = deque([tuple(start)])
        visited = set([tuple(start)])
        while dq:
            curr_x, curr_y = dq.popleft()
            for move in ((1,0), (-1,0), (0,1), (0,-1)):
                next_move = get_next_pos(curr_x, curr_y, move)
                if next_move not in visited:
                    if next_move == dest_tuple:
                        return True
                    dq.append(next_move)
                    visited.add(next_move)
        return False
                
                    
                    
        