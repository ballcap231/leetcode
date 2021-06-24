class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #Best case  - when all numbers are the minimum val except for one:
        #E.g. [1,1,1,1,4] - only "max - min" operations
        #Worst case - when all numbers are the maximum val except for one:
        #E.g. [1,4,4,4,4,4] - "max - min" operations 5 times (i.e. 15)
        
        
        #O(N) time and O(1) space
        min_val = min(nums)
        count = 0
        for val in nums:
            count += val - min_val
        return count
        

        # O(NlogN) time and O(N) or O(1) space depending on if in-place sort allowed
        # nums.sort()
        # count = 0
        # for pos in range(len(nums) - 1, 0, -1):
        #     count += nums[pos] - nums[0]
        # return count
        
        
        #O(N) time and O(1) space
        # return sum(nums)-len(nums)*min(nums)