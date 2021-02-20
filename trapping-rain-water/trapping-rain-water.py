class Solution:
    def trap(self, height: List[int]) -> int:
        left = left_max = right_max = 0
        right = len(height) - 1
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    water += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    water += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return water
    
        
        
        
        
        
        
        
#         start = end = None
#         for pos, val in enumerate(height):
#             if val > 0:
#                 if start is not None:
#                     end = pos
#                 if start is None:
#                     start = pos
            
#         if end is None:
#             return 0
#         max_level = max(height)
#         water = 0
        
#         for level in range(1, max_level + 1):
#             left = float('inf')
#             for right in range(start, end + 1):
#                 if height[right] >= level:
#                     if right > left + 1:
#                         water += right - left - 1
#                     left = right
        
#         return water
                
                
                
        