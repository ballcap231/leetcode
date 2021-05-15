class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        pos = 0
        smallest = 1
        while pos < len(nums) and nums_sort[pos] <= smallest:
            if nums_sort[pos] == smallest:
                smallest += 1
            pos += 1
        return smallest