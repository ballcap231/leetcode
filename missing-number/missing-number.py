class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #O(N) time and O(1) space
        #arithmetic sum - n/2 (a1 + an)
        
        arthmetic_sum = (len(nums) + 1) * (0 + len(nums)) // 2
        
        return arthmetic_sum - sum(nums)