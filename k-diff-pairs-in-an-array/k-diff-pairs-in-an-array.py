class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums)
        set_nums = set()
        count = 0
        r = 0
        while r < len(nums):
            curr_num = nums_sorted[r]
            if curr_num - k in set_nums or curr_num + k in set_nums:
                count += 1
                set_nums.add(curr_num)
                while r < len(nums) and nums_sorted[r] == curr_num:
                    r += 1
                continue
            set_nums.add(curr_num)
            r += 1
        return count
        
        
        

        
#         set_nums = set()
#         count = 0
        
#         for num in set_nums:
#             if num - k in set_nums or num + k in set_nums:
                