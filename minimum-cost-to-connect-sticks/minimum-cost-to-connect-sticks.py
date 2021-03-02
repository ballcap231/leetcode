class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heapq.heapify(sticks)
        ret = 0
        while len(sticks) >= 2:
            s1,s2 = heapq.heappop(sticks),heapq.heappop(sticks)
            s3 = s1 + s2
            ret += s3
            heapq.heappush(sticks, s3)
        
        return ret