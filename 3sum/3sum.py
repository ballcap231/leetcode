class Solution(object):
    
    #At this point, list is sorted
    def twoSum(self,start,end, k):
        if start == end:
            return []
        res = []
        while start<end:
            s = self.nums[start]+self.nums[end]
            if s>k:
                end-=1
            elif s<k:
                start+=1
            else:
                res.append([self.nums[start],self.nums[end]])
                # Check for duplicate pointers so we dont post duplicate sum combinations
                while start < end and self.nums[start] == self.nums[start+1]:
                    start += 1
                while start < end and self.nums[end] == self.nums[end-1]:
                    end -= 1
                start+=1
                end-=1
        return res                
    
    def threeSum(self, nums):
        #O(N^2) and O(N) space
        if len(nums)<3:
            return []
        
        self.nums = sorted(nums)
        res = []
        
        for i in range(len(self.nums)):
            if i > 0  and self.nums[i] == self.nums[i - 1]:
                continue
            k = -self.nums[i]
            tmp = self.twoSum(start = i+1,end = len(self.nums) - 1, k = k)
            for t in tmp:
                res.append([self.nums[i],t[0],t[1]])        
        
        return res