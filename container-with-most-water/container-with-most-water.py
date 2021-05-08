class Solution:
    def maxArea(self, height: List[int]) -> int:       
        # O(N) time and O(1) space - 2 pointer approach
        L,R = 0, len(height) - 1
        max_height = 0
        while L < R:
            max_height = max(max_height, min(height[L],height[R]) * (R - L))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return max_height
        
        # #O(N^2) time and O(1) space - Brute Force
        # max_height = 0
        # for L in range(len(height) - 1):
        #     for R in range(L + 1, len(height)):
        #         max_height = max(max_height, min(height[R], height[L]) * (R - L))
        # return max_height 