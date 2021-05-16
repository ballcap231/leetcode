class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # Brute Force - O(NlogN) time and O(N) or O(1) space
        # nums_sort = sorted(nums)
        # pos = 0
        # smallest = 1
        # while pos < len(nums) and nums_sort[pos] <= smallest:
        #     if nums_sort[pos] == smallest:
        #         smallest += 1
        #     pos += 1
        # return smallest
        
        #In-place Index hashing - O(N) time and O(1) space
        if 1 not in nums:
            return 1
        
        if len(nums) == 1:
            return 2

        
        for pos in range(len(nums)):
            if nums[pos] <= 0 or nums[pos] > len(nums):
                nums[pos] = 1
        
        for pos in range(len(nums)):
            abs_num = abs(nums[pos])
            if abs_num == len(nums):
                nums[0] = - abs(nums[0])
            else:
                nums[abs_num] = - abs(nums[abs_num])
        for pos in range(1, len(nums)):
            if nums[pos] > 0:
                return pos
        if nums[0] > 0:
            return len(nums)
        return len(nums) + 1

        
        