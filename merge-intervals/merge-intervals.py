class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(NlogN) time and O(N) space
        #even if we can sort in-place, intervals.sort() still takes O(N) space
        if len(intervals) < 2:
            return intervals
        sorted_ls = sorted(intervals, key = lambda x: x[0])
        new_ls = [sorted_ls[0]]
        for ls in sorted_ls[1:]:
            if ls[0] <= new_ls[-1][1]:
                new_ls[-1][1] = max(new_ls[-1][1], ls[1])
            else:
                new_ls.append(ls)
        return new_ls
        
        
        
        
        
        
#         if not intervals:
#             return []
#         sorted_ls = sorted(intervals,key = lambda x: x[0])
#         curr = sorted_ls[0]
#         new_ls = []
#         for ls in sorted_ls[1:]:
#             if ls[0] <= curr[1]:
#                 curr[1] = max(curr[1],ls[1])
#             else:
#                 new_ls.append(curr)
#                 curr = ls
#         new_ls.append(curr)
        
#         return new_ls