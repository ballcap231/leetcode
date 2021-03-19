class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        #O(N^2) time and O(N^2) space because board is a N x N square 
        #using BFS
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
            for pos_2 in range(pos + 1, min(N*N + 1, pos + 7)):
                row, col = get_pos(pos_2)
                if board[row][col] > -1:
                    pos_2 = board[row][col]
                if pos_2 == N * N:
                    return pos_moves[pos] + 1
                if pos_2 not in pos_moves:
                    deq.append(pos_2)
                    pos_moves[pos_2] = pos_moves[pos] + 1
        return -1