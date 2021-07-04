class Solution(object):
    #At this point, list is sorted
    def twoSum(self,start,end, k):
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
        
        for i in range(len(self.nums) - 2):
            if i > 0  and self.nums[i] == self.nums[i - 1]:
                continue
            k = -self.nums[i]
            tmp = self.twoSum(start = i+1,end = len(self.nums) - 1, k = k)
            for t in tmp:
                res.append([self.nums[i],t[0],t[1]])        
        
        return res
    # def threeSum(self, nums):
        # #Brute Force
        # #O(N^3) time and O(1) auxillary space
        # output = []
        # nums.sort()
        # if len(nums) < 3 or nums[0] >= 1 or nums[-1] < 0: return []
        # soln = set()
        # for xx in range(len(nums) - 2):
        #     for yy in range(xx + 1, len(nums) - 1):
        #         for zz in range(yy + 1, len(nums)):
        #             if nums[xx] + nums[yy] + nums[zz] == 0:
        #                 soln.add(tuple(sorted([nums[xx],nums[yy],nums[zz]])))
        # return list(soln)
    
    
    
    
    
