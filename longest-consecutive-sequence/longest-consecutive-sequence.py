class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        max_len = 0
        curr_len = 0
        for pos in range(len(nums)):
            if not curr_len or nums[pos - 1] + 1 == nums[pos]:
                curr_len += 1
            elif nums[pos - 1] == nums[pos]:
                continue
            else:
                curr_len = 1
            max_len = max(max_len, curr_len)
        return max_len
                
            