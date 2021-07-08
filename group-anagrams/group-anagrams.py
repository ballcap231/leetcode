from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # #Bucket Sort on ASCII values
        # #O(N * K) time where N == |strs|, K == length of words ins strs
        # #O(N * K) space
        # dd = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     dd[tuple(count)].append(s)
        # return dd.values()

        
        dd = defaultdict(list)
        for s in strs:
            #Can make array of 200 if you can't remember relative ordering of ascii values
            count = [0] * 200
            for c in s:
                count[ord(c)] += 1
            dd[tuple(count)].append(s)
        return dd.values()
    
        
        
#         #frozenset on strings
#         #O(N * K) time where N == |strs|, K == length of words ins strs
#         #O(N * K) space
#         dd = defaultdict(list)
#         for s in strs:
#             dd[frozenset(Counter(s).items())].append(s)
#         return dd.values()
    
#         #Sorting on strings
#         #O(N * K * log(K)) time where N == |strs|, K == length of words ins strs
#         #O(N * K) space
#         dd = defaultdict(list)
#         for s in strs:
#             dd[tuple(sorted(Counter(s).items()))].append(s)
#         return dd.values()