class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        last_pos = 0
        for curr_pos in range(1,len(nums)):
            if nums[last_pos] != nums[curr_pos]:
                last_pos += 1
                nums[last_pos] = nums[curr_pos]
        
        return last_pos + 1