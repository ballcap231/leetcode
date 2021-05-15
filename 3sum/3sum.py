# from collections import Counter
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         soln_ls = []
#         soln_counters = []
#         length = len(nums)
#         if length < 3:
#             # returning empty list if less than 3 objects in nums
#             return soln_ls
        
        
#         for counter_iter,iter_ in enumerate(nums):
#             if counter_iter == length - 2 :
#                 #exiting if trying to access 2nd to last object
#                 return soln_ls
#             #Executing 2 sum algorithm
#             for counter_ii, ii in enumerate(nums[counter_iter + 1:]):
#                 rest_of_list_index = counter_iter + counter_ii + 2
#                 sum_of_first_2 = iter_ + ii
#                 neg_of_first_2 = -sum_of_first_2
#                 if neg_of_first_2 in nums[rest_of_list_index:]:
#                     sum3_ls = [iter_,ii,neg_of_first_2]
#                     sum3_counter = Counter(sum3_ls)
#                     #checking for duplicates - if duplicate don't execute if statement
#                     if sum3_counter not in soln_counters:
#                         soln_counters.append(sum3_counter)
#                         soln_ls.append(sum3_ls)
                    
    
    
class Solution(object):
    
    #At this point, list is sorted
    def twoSum(self,nums, k):
        if len(nums)==0:
            return nums
        p1=0
        p2=len(nums)-1
        res = []
        while p1<p2:
            s = nums[p1]+nums[p2]
            if s>k:
                p2-=1
            elif s<k:
                p1+=1
            else:
                res.append([nums[p1],nums[p2]])
                p1+=1
                p2-=1
        return res                
    
    def threeSum(self, nums):
        if len(nums)<3:
            return []
        
        nums = sorted(nums)
        res = set()
        
        for i in range(len(nums)):
            k = -nums[i]
            tmp = self.twoSum(nums[i+1:],k)
            if len(tmp)!=0:
                for t in tmp:
                    res.add( (nums[i],t[0],t[1])  )             
        
        lres = []
        for s in res:
            lres.append([s[0],s[1],s[2]])
        
        return(lres)     