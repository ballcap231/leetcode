class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [xx for xx in range(1,10)]
        res = []
        
        def backtrack(cur_pos, cur_sum, cur_stack):
            for pos in range(cur_pos, len(candidates)):
                new_sum = cur_sum + candidates[pos]
                if new_sum == n and len(cur_stack) + 1 == k:
                    res.append(cur_stack + [candidates[pos]])
                    break
                if new_sum > n or len(cur_stack) + 1 > k:
                    break
                backtrack(pos + 1, new_sum, cur_stack + [candidates[pos]])
        backtrack(0,0,[])
        return res
        
        
        
        
        
        
        
        
#         ans = []
#         self.count = 0
#         def backtrack(candidates, cum_sum, stack, cum_count):
#             self.count += 1
#             for count, cand in enumerate(candidates):
#                 if cum_sum + cand == n and cum_count + 1 == k:
#                     ans.append(stack + [cand])
#                     continue
#                 if cum_sum + cand >= n:
#                     continue
#                 if cum_count + 1 >= k:
#                     continue
#                 backtrack(candidates[count + 1:],cum_sum + cand, stack + [cand], cum_count + 1)
                
#         backtrack([1,2,3,4,5,6,7,8,9], 0, [], 0)
#         print(self.count)
#         return ans