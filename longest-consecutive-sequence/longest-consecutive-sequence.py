class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #O(N) time and space
        nums_set = set(nums)
        max_len = 0
        
        for val in nums:
            if val in nums_set:
                curr_len = 1
                nums_set.discard(val)
                #counting nums greater than val
                greater_num = val + 1
                while greater_num in nums_set:
                    curr_len += 1
                    nums_set.discard(greater_num)
                    greater_num += 1
                #counting nums less than val
                lesser_num = val - 1
                while lesser_num in nums_set:
                    curr_len += 1
                    nums_set.discard(lesser_num)
                    lesser_num -= 1
                #tracking max conseq subseq so far
                max_len = max(max_len, curr_len)
        return max_len
        
        
        
        
#         #O(NlogN) time and O(1) space or O(N) space if can't modify input arr
#         #Brute force
#         nums.sort()
        
#         max_len = 0
#         curr_len = 0
#         for pos in range(len(nums)):
#             if not curr_len or nums[pos - 1] + 1 == nums[pos]:
#                 curr_len += 1
#             elif nums[pos - 1] == nums[pos]:
#                 continue
#             else:
#                 curr_len = 1
#             max_len = max(max_len, curr_len)
#         return max_len
                
            