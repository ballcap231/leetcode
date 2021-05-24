class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        new_nums = []
        
        p1 = p2 = 0
        
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                new_nums.append(nums1[p1])
                p1 += 1
            else:
                new_nums.append(nums2[p2])
                p2 += 1
        
        if p1 >= m:
            while p2 < n:
                new_nums.append(nums2[p2])
                p2 += 1
        else:
            while p1 < m:
                new_nums.append(nums1[p1])
                p1 += 1 
        
        for ii in range(len(nums1)):
            nums1[ii] = new_nums[ii]
        
        
        
        
        
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         # nums1[:] = sorted(nums1[:m] + nums2)
#         # two get pointers for nums1 and nums2
#         p1 = m - 1
#         p2 = n - 1
#         # set pointer for nums1
#         p = m + n - 1
        
#         # while there are still elements to compare
#         while p1 >= 0 and p2 >= 0:
#             if nums1[p1] < nums2[p2]:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1
#             else:
#                 nums1[p] =  nums1[p1]
#                 p1 -= 1
#             p -= 1
        
#         # add missing elements from nums2
#         nums1[:p2 + 1] = nums2[:p2 + 1]