class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         sorted_candidates = sorted(candidates, reverse = True)
        
#         for val in range(len(candidates)):
            
#         def n_choose_k(pos, k, res_arr):
#             for pos, cand in enumerate(candidates):
#                 cum_sum = cand
#                 while cum_sum  < target:
                    
            
        
#         for k in range(n):
#             n_choose_k(k,[])
        
        
        # sorted_candidates = sorted(candidates, reverse = True)
        ans = []
        def backtrack(candidates, cum_sum, stack):
            for count, cand in enumerate(candidates):
                if cum_sum + cand > target:
                    continue
                if cum_sum + cand == target:
                    ans.append(stack + [cand])
                    continue
                backtrack(candidates[count:], cum_sum + cand, stack + [cand])
                
                
        backtrack(candidates, 0, [])
        return ans