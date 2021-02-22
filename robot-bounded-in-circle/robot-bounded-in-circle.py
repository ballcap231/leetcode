class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        direction = 0 # 0,1,2,3,for N,E,S,W respectively
        pos = [0,0]
        for vec in instructions:
            if vec == 'L':
                direction = (direction + 3) % 4
            elif vec == 'R':
                direction = (direction + 1) % 4
            else:
                pos[0] += directions[direction][0]
                pos[1] += directions[direction][1]

        return direction != 0 or (pos[0] == 0 and pos[1] == 0)
                
            