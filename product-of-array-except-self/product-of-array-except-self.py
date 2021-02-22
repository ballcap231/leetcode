class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(N) time and O(1) auxillary space - i.e. not counting output array 
        if not nums or len(nums) < 2:
            return []
        
        prod_arr = [0 for _ in range(len(nums))]
        prod_arr[0] = 1
        for ii in range(1, len(nums)):
            prod_arr[ii] = nums[ii - 1] * prod_arr[ii - 1]
        
        R = 1
        for ii in reversed(range(len(nums))):
            prod_arr[ii] *= R
            R *= nums[ii]
        return prod_arr
        
            