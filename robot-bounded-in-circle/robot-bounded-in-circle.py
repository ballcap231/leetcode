class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #O(N) time and O(1) space
# the robot is already back to its origin by the end of the string traversal, and
# the robot is away from the origin, but heading to a direction different from its initial direction. For example, if the robot is facing left by the end of the first string traversal, after three other traversals of left->left->left, it is back to the origin. A second example is that if the robot is facing down by the end of the first string traversal, it only takes another traversal for it to get back to the origin.

#         directions = [[0,1],[1,0],[0,-1],[-1,0]]
#         direction = 0 # 0,1,2,3,for N,E,S,W respectively
#         pos = [0,0]
#         for vec in instructions:
#             if vec == 'L':
#                 direction = (direction + 3) % 4
#             elif vec == 'R':
#                 direction = (direction + 1) % 4
#             else:
#                 pos[0] += directions[direction][0]
#                 pos[1] += directions[direction][1]

#         return direction != 0 or (pos[0] == 0 and pos[1] == 0)
                
        
        
        directions = [[0,1], [1,0], [0,-1],[-1,0]]
        direction = 0
        pos = [0,0]
        for ii in range(4):
            for vec in instructions:
                if vec == 'L':
                    direction = (direction + 3) % 4
                elif vec == 'R':
                    direction = (direction + 1) % 4
                else:
                    pos[0] += directions[direction][0]
                    pos[1] += directions[direction][1]
        
        return pos[0] == 0 and pos[1] == 0
        
        