class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
        
        
        
#         # my solution (not LC soln).... what time complexity is this??? - may not be best.
#         if not nums:
#             return [[]]
#         ls = []
        
#         for count, val in enumerate(nums):
#             if count != 0:
#                 for sub_count, sub_ls in enumerate(ls):
#                     if sub_count == 0:
#                         new_ls = [sub_ls[:x] + [val] + sub_ls[x:] for x in range(len(sub_ls) + 1)]
#                     else:
#                         new_ls += [sub_ls[:x] + [val] + sub_ls[x:] for x in range(len(sub_ls) + 1)]
#                 ls = new_ls
#             else:
#                 ls += [[val]]
#         return ls
        