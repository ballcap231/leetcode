class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyer-Moore voting algorithm
        #O(N) time and O(1) space
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
        return candidate
    
        #Hashmap - O(N) time and space
        # counts = collections.Counter(nums)
        # return max(counts,key=lambda xx:counts[xx])
        

            