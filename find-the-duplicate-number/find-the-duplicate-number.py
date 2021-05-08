class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0],nums[0]
        n = len(nums)
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        # s = 1
        # for num in nums:
        #     if s >> num & 1:
        #         return num
        #     s |= 1<<num