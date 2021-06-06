class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        if len(counts) == 1:
            return 0
        min_val = min(nums)
        
        hq = []
        moves = 0
        #Sorting values in buckets
        for val, counts in counts.items():
            heapq.heappush(hq, (-val, counts))
        
        #Loop until the only value in heap is the minimum value - only minimum val left
        while hq[0][0] != -min_val:
            curr_val, curr_count = heapq.heappop(hq)
            moves += curr_count
            next_val, next_count = heapq.heappop(hq)
            heapq.heappush(hq, (next_val, next_count + curr_count))
        
        return moves
            