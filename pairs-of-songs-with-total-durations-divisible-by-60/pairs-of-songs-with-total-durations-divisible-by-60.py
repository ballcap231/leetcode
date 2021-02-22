class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        buckets = [0 for xx in range(60)]
        
        for t in time:
            buckets[t % 60] += 1
            
        tot = 0
        
        for l in range(1,30):
            tot += buckets[l] * buckets[60 - l]
        
        def n_choose_2(val):
            return val * (val - 1) // 2
        tot += n_choose_2(buckets[0]) + n_choose_2(buckets[30])
        return tot
        