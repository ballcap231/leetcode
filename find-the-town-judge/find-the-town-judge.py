from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
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
        
        
        
#         #if only one guy, he must be the judge 
#         if N == 1:
#             return 1
        
#         trustees = defaultdict(int)
#         trusters = defaultdict(int)

        
#         for t_pair in trust:
#             trustees[t_pair[1]] += 1
#             trusters[t_pair[0]] += 1
            
#         set_trustees = set(trustees.keys())
#         set_trusters = set(trusters.keys())
#         #relative complement of for trustees must contain only the judge
#         trustees_relative_complement = set_trustees - set_trusters
        
#         # town_judge = next(iter(trustees_relative_complement))
        
#         #can't index a set so iterate it once instead (for loop is apparently fastest way but next(iter()) is fast too but StopIteration Error is called if set is empty which is not what we want)
#         for ii in trustees_relative_complement:
#             town_judge = ii
        
#         #if the relative complement doesn't equal 1, then there's either no judge (less than 1) or more than 1 possible judges(greater than 1)
#         if len(trustees_relative_complement) != 1:
#             return -1
#         #if the number of people who trust the potential judge does not match the number of trusters, then the judge is one of the trusters or not all the trusters trust the judge
#         if trustees[town_judge] != len(set_trusters):
#             return -1
        
#         return town_judge