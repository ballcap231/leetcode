class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        count_ls = [(-values, keys) for keys, values in counts.items()]
        
        heapq.heapify(count_ls)
        
        ret = []
        
        for _ in range(k):
            ret.append(heapq.heappop(count_ls)[1])
        return ret