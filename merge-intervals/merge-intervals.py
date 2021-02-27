class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(NlogN) time and O(N) space - if we can't edit intervals
        #even if we can sort in-place, intervals.sort() still takes O(N) space
#         if len(intervals) < 2:
#             return intervals
#         sorted_ls = sorted(intervals, key = lambda x: x[0])
#         new_ls = [sorted_ls[0]]
#         for ls in sorted_ls[1:]:
#             if ls[0] <= new_ls[-1][1]:
#                 new_ls[-1][1] = max(new_ls[-1][1], ls[1])
#             else:
#                 new_ls.append(ls)
#         return new_ls
    
        #O(NlogN) time and O(1) space - makes edits to intervals
        #using heapsort
        if len(intervals) < 2:
            return intervals
        
        heapq.heapify(intervals)
        new_ls = [heapq.heappop(intervals)]
        
        for ii in range(len(intervals)):
            if new_ls[-1][1] >= intervals[0][0]:
                new_ls[-1][1] = max(new_ls[-1][1], heapq.heappop(intervals)[1])
            else:
                new_ls.append(heapq.heappop(intervals))

        return new_ls
