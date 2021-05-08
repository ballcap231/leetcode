class Solution:
    def maxArea(self, height: List[int]) -> int:
        L,R = 0, len(height) - 1
        max_height = 0
        while L < R:
            max_height = max(max_height, min(height[L],height[R]) * (R - L))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return max_height