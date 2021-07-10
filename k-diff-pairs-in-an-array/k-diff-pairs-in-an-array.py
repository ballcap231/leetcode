class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        #O(N) time and space
        result = 0
        counter = Counter(nums)

        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
            elif k < 0 and x - k in counter:
                result += 1
        return result
        
        
        
        # #O(NlogN) time and O(N) space
        # nums_sorted = sorted(nums)
        # set_nums = set()
        # count = 0
        # r = 0
        # while r < len(nums):
        #     curr_num = nums_sorted[r]
        #     if curr_num - k in set_nums or curr_num + k in set_nums:
        #         count += 1
        #         set_nums.add(curr_num)
        #         while r < len(nums) and nums_sorted[r] == curr_num:
        #             r += 1
        #         continue
        #     set_nums.add(curr_num)
        #     r += 1
        # return count