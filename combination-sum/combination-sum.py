class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #N-ary DFS using backtracking 
        #O(N^(T/M)) time and O(T/M) space 
        #where T is target, M is minimum value in candidates and
        #N is the length of candidates
        self.sorted_candidates = sorted(candidates, reverse = True)
        ans = []
        def backtrack(start_pos, cum_sum, stack):
            for count in range(start_pos, len(self.sorted_candidates)):
                cand = self.sorted_candidates[count]
                if cum_sum + cand > target:
                    continue
                if cum_sum + cand == target:
                    ans.append(stack + [cand])
                    continue
                backtrack(count, cum_sum + cand, stack + [cand])
                
                
        backtrack(0, 0, [])
        return ans
    
    