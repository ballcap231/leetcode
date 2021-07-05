class Solution(object):
#     #At this point, list is sorted
#     def twoSum(self,start,end, k):
#         res = []
#         while start<end:
#             s = self.nums[start]+self.nums[end]
#             if s>k:
#                 end-=1
#             elif s<k:
#                 start+=1
#             else:
#                 res.append([self.nums[start],self.nums[end]])
#                 # Check for duplicate pointers so we dont post duplicate sum combinations
#                 while start < end and self.nums[start] == self.nums[start+1]:
#                     start += 1
#                 while start < end and self.nums[end] == self.nums[end-1]:
#                     end -= 1
#                 start+=1
#                 end-=1
#         return res                
    
#     def threeSum(self, nums):
#         #O(N^2) and O(N) auxiliary space or O(N^2) including output space
#         if len(nums)<3:
#             return []
        
#         self.nums = sorted(nums)
#         res = []
        
#         for i in range(len(self.nums) - 2):
#             if i > 0  and self.nums[i] == self.nums[i - 1]:
#                 continue
#             k = -self.nums[i]
#             tmp = self.twoSum(start = i+1,end = len(self.nums) - 1, k = k)
#             for t in tmp:
#                 res.append([self.nums[i],t[0],t[1]])        
        
#         return res

    # def threeSum(self, nums):
    #     #Brute Force
    #     #O(N^3) time and O(N) auxiliary space or O(N^2) including output space
    #     output = []
    #     soln = set()
    #     for xx in range(len(nums) - 2):
    #         for yy in range(xx + 1, len(nums) - 1):
    #             for zz in range(yy + 1, len(nums)):
    #                 if nums[xx] + nums[yy] + nums[zz] == 0:
    #                     soln.add(tuple(sorted([nums[xx],nums[yy],nums[zz]])))
    #     return soln
    
#     def threeSum(self, nums):
#         #O(N^2) time and O(N) auxiliary space or O(N^2) including output space
#         duplicates = set()
#         ret = set()
        
#         for first_pos, first_num in enumerate(nums):
#             if first_num not in duplicates:
#                 duplicates.add(first_num)
#                 first_num_combos = set()
#                 for second_pos in range(first_pos + 1, len(nums)):
#                     second_num = nums[second_pos]
#                     third_num = -(first_num + second_num)
#                     if third_num in first_num_combos:
#                         ret.add(tuple(sorted([first_num, second_num, third_num])))
#                     first_num_combos.add(second_num)
#         return ret
    
    def threeSum(self, nums):
        def kSum(nums, target, k):
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []
            if k == 2:
                return twoSum(nums, target)
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums, target):
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return res

        nums.sort()
        target = 0
        return kSum(nums, target, 3)
    
    
