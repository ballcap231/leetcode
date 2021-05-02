# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         self.count =  0
#         def backtrack(first = 0, curr = []):
#             # if the combination is done
#             if len(curr) == k:  
#                 output.append(curr[:])
#             for i in range(first, n):
#                 self.count += 1
#                 # add nums[i] into the current combination
#                 curr.append(nums[i])
#                 # use next integers to complete the combination
#                 backtrack(i + 1, curr)
#                 # backtrack
#                 curr.pop()
        
#         output = []
#         n = len(nums)
#         for k in range(n + 1):
#             backtrack()
#         print("Final output size: " + str(len(output)) + 
#               ' vs # recursion calls: ' + str(self.count))
#         return output

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		# self.count = 0
		self.ans = []
        #O(N * 2^N) time and space
        #O(N) space if we don't count output array as part of space to hold prev_combo
        #Because there are 2^N possible sets (each element is in or not in a set)
        #In each set, there is a possibility of up to N elements
		def n_choose_k(n, k, prev_combo):
			for count, val in enumerate(n):
				# self.count += 1
				#stopping further exploration because 
				#it's not possible to create large enough combinations anymore
				if len(prev_combo) + len(n) - count < k:
					return
				if len(prev_combo) + 1 == k:
					#appending only [val] instead of creating copy of list using [:]
					#[:] creates shallow copy which takes O(N) time
					self.ans.append(prev_combo + [val]) 
					continue
				n_choose_k(n[count + 1:], k, prev_combo + [val])

		for k in range(1,len(nums) + 1):
			n_choose_k(nums, k, [])

		self.ans.append([])
		# print("Final output size: " + str(len(self.ans)) + 
		# 	  ' vs # recursion calls: ' + str(self.count))
		return self.ans