class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # Bucket Sort-Like, O(N) time and space
#         # No sorting necessary inside buckets
#         # 'Sorting' happens by relative bucketing
#         buckets = [[] for xx in range(len(nums))]
#         counts = Counter(nums)
#         for num, count in counts.items():
#             buckets[count - 1].append(num)
        
#         ret_ls = []
#         for bucket in buckets:
#             for val in bucket:
#                 ret_ls.append(val)
#         return ret_ls[-k:]
    
        counts = Counter(nums)
        most_common = [key_val_tuple[0] for key_val_tuple in counts.most_common(k)]
        return most_common
    
    
            
#         #Heap
#         #O(N + KlogN) time and O(N) space, where K == k, N == |nums|
#         counts = Counter(nums)
#         count_ls = [(-values, keys) for keys, values in counts.items()]
#         heapq.heapify(count_ls)
#         ret = []

#         for _ in range(k):
#             ret.append(heapq.heappop(count_ls)[1])
#         return ret