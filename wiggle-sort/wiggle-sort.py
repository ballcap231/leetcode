class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for ii in range(len(nums)):
            nums[ii:ii+2] = sorted(nums[ii:ii+2], reverse = ii % 2) 