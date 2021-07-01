class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) >= len(nums2):
            long, short = nums1, nums2
        else:
            long, short = nums2, nums1
        l_len, s_len = len(long) , len(short)
        
        M_ind = (l_len + s_len - 1) // 2
        
        lo, hi = 0, s_len
        
        while lo < hi:
            med = (lo + hi) //2
            if (M_ind - med - 1 < 0 or short[med] >= long[M_ind - med - 1]):
                hi = med
            else:
                lo = med + 1
        med = lo
        
        ls = sorted(short[med:med+2] + long[M_ind - med: M_ind - med + 2])
        
        if (l_len + s_len) % 2 == 1:
            return ls[0]
        else:
            return (ls[0] + ls[1]) / 2
            