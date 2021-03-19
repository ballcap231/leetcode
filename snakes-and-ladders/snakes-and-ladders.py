class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        
        deq = deque()
        deq.append(1)
        pos_moves = {1:0}
        def get_pos(pos):
            quot, rem = divmod(pos - 1, N)
            
            row = N - 1 - quot
            col = rem if row%2 != N%2 else N - rem - 1
            return row, col
        
        while deq:
            pos = deq.popleft()
            if pos == N * N:
                return pos_moves[pos]
            for pos_2 in range(pos + 1, min(N*N + 1, pos + 7)):

                row, col = get_pos(pos_2)
                if board[row][col] > -1:
                    pos_2 = board[row][col]
                if pos_2 in pos_moves:
                    continue
                deq.append(pos_2)
                pos_moves[pos_2] = pos_moves[pos] + 1
                
        return -1
#         N = len(board)

#         def get(s):
#             # Given a square num s, return board coordinates (r, c)
#             quot, rem = divmod(s-1, N)
#             row = N - 1 - quot
#             col = rem if row%2 != N%2 else N - 1 - rem
#             return row, col
#         dist = {1: 0}
#         queue = collections.deque([1])
#         while queue:
#             s = queue.popleft()
#             if s == N*N: return dist[s]
#             for s2 in range(s+1, min(s+6, N*N) + 1):
#                 r, c = get(s2)
#                 if board[r][c] != -1:
#                     s2 = board[r][c]
#                 if s2 not in dist:
#                     dist[s2] = dist[s] + 1
#                     queue.append(s2)
#         return -1