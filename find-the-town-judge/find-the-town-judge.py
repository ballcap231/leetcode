class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        #O(E) time where E is number of edges
        #O(N) space
        if len(trust) < N - 1: return -1
        candidates = set(xx for xx in range(1, N + 1))
        
        outbound = defaultdict(set)
        inbound = defaultdict(set)
        
        for edge in trust:
            candidates.discard(edge[0])
            outbound[edge[0]].add(edge[1])
            inbound[edge[1]].add(edge[0])
        
        for cand in candidates:
            if len(inbound[cand]) == N - 1:
                return cand
        return -1
