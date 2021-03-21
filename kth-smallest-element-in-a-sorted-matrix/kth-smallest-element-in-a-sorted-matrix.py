import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        rows = min(len(matrix), k)
        cols = len(matrix[0])
        my_heap = []
        for row in range(rows):
            heapq.heappush(my_heap,(matrix[row][0],row,0))
        
        count = 1
        while count < k:
            elem = heapq.heappop(my_heap)
            row,col = elem[1],elem[2]
            if col + 1 < cols:
                heapq.heappush(my_heap, (matrix[row][col + 1],row,col + 1))
            count += 1
            
        return heapq.heappop(my_heap)[0]
            
        