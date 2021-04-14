class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        replace_pos = last_pos = 1
        
        pos = 1
        while pos < len(nums):
            if nums[pos] == nums[pos - 1]:
                break
            pos += 1
        replace_pos = last_pos = pos
        print(replace_pos, last_pos, pos)
        for pos in range(last_pos + 1,len(nums)):
            if nums[last_pos] != nums[pos]:
                nums[replace_pos] = nums[pos]
                replace_pos += 1
                last_pos = pos
        return replace_pos
    #[-5,-5,-5,-2,0,1,4,5,5,6,7,22,22,22,51,7442]