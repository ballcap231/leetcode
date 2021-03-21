class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         if image[sr][sc] == newColor:
#             return image
        
        
        
        
        # n, m = len(image), len(image[0])
        # stack = [[sr, sc]]
        # oldColor = image[sr][sc]
        # if oldColor == newColor: return image
        # while stack:
        #     x, y = stack.pop()
        #     image[x][y] = newColor
        #     for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
        #         nx, ny = x+dx, y+dy
        #         if (0 <= nx < n) and (0 <= ny < m):
        #             if image[nx][ny] == oldColor:
        #                 stack.append([nx, ny])
        # return image
        
        row = len(image)
        col = len(image[0])
        color = image[sr][sc]
        
        if color == newColor:
            return image
        
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r-1, c)
                if r < row-1:
                    dfs(r+1, c)
                if c >= 1:
                    dfs(r, c-1)
                if c < col-1:
                    dfs(r, c+1)
        
        dfs(sr, sc)
        
        return image