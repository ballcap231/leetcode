class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        c1 = Counter()
        
        for val in nums1:
            c1[val] += 1
        
        print(c1,nums1)
        ret = []
        for val in nums2:
            if val in c1:
                ret.append(val)
                c1[val] -= 1
                if not c1[val]:
                    c1.pop(val)
        
        return ret
            
        
        