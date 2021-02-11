from collections import deque
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        q = deque([0,0])
        for pos in range(len(nums)):
            jump_val = q[0] + nums[pos]
            new_val = max(q[1], jump_val)
            q.popleft()
            q.append(new_val)
        
        return q[-1]