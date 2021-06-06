class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        #O(NlogN) time and O(N) space
        counts = Counter(nums)
        if len(counts) == 1:
            return 0
        
        hq = []
        moves = 0
        #Sorting values in buckets
        for val, counts in counts.items():
            heapq.heappush(hq, (-val, counts))
        
        #Loop until the only value in heap is the minimum value - only minimum val left
        while len(hq) > 1:
            curr_val, curr_count = heapq.heappop(hq)
            moves += curr_count
            hq[0] = (hq[0][0], hq[0][1] + curr_count)
        
        return moves
            