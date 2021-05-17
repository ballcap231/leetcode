class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #O(N! / (N - N)! * N) or O(N! * N) time
        #O(N! * N) space
        res = []
        
        def backtrack(first_pos):
            if first_pos == len(nums):
                res.append(nums[:])
            else:
                for pos in range(first_pos, len(nums)):
                    nums[pos],nums[first_pos] = nums[first_pos], nums[pos]

                    backtrack(first_pos + 1)
                    nums[pos],nums[first_pos] = nums[first_pos], nums[pos]
        backtrack(0)
        return res
            
        
        # ans = []
        # def backtrack(prev_cand, candidates):
        #     for count, cand in enumerate(candidates):
        #         if len(prev_cand) + 1 == len(nums):
        #             ans.append(prev_cand + [cand])
        #         else:
        #             backtrack(prev_cand + [cand], candidates[:count] + candidates[count + 1:])
        # backtrack([], nums)
        # return ans
        
        
        

        