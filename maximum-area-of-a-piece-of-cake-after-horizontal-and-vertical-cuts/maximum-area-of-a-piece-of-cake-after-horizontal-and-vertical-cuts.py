class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        prev_h = prev_v = max_h = max_v = 0
        
        for cut_h in sorted(horizontalCuts):
            max_h = max(max_h, cut_h - prev_h)
            prev_h = cut_h
        
        max_h = max(max_h, h - prev_h)
        
        for cut_v in sorted(verticalCuts):
            max_v = max(max_v, cut_v - prev_v)
            prev_v = cut_v
        
        max_v = max(max_v, w - prev_v)
        
        return (max_v * max_h) % (10 ** 9 + 7)
        