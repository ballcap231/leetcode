class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #O(N) time and O(1) space - 1 loop
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l],nums[r] = nums[r], nums[l]
                l += 1
        
        # 2 Loops
#         #O(N) time and O(1) space
#         l = 0
#         for r in range(len(nums)):
#             if nums[r] != 0:
#                 nums[l] = nums[r]
#                 l += 1
#         for l in range(l, len(nums)):
#             nums[l] = 0
        