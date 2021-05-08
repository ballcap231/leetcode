class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #O(N) time and O(1) space - DP
        max_alt = 0
        curr_alt = 0
        for alt in gain:
            curr_alt += alt
            max_alt = max(max_alt, curr_alt)
        
        return max_alt
        