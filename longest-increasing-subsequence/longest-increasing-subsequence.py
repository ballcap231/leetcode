class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_subseq = 1
        subseq = [1]
        
        for pos in range(1, len(nums)):
            longest_seq = 1
            for sub_pos, sub_num in enumerate(subseq):
                if nums[sub_pos] < nums[pos]:
                    longest_seq = max(longest_seq, sub_num + 1)
            max_subseq = max(max_subseq, longest_seq)
            subseq.append(longest_seq)
        return max_subseq
        
        
        
        
        #O(N^2) time and O(N) space
#         subseq = []
#         max_seq = 0
#         for pos, val in enumerate(nums):
#             max_subseq = 1
#             for pos_sub, val_sub in enumerate(nums[:len(subseq)]): 
#                 if val_sub < val:
#                     max_subseq = max(max_subseq, subseq[pos_sub] + 1)
#             max_seq = max(max_seq,max_subseq)
#             subseq.append(max_subseq)
#         return max_seq

        #O(NLogN) Time and O(N) space
        #very similar to 334. Increasing Triplet Subsequence
        tails = []
        for num in nums:
            i = bisect_left(tails, num) #finds first number in tails that is larger than or equal to num to replace
            #if everything in tails is smaller than num then append
            if i == len(tails):
                tails.append(num)
            tails[i] = num #replace the number that was bisected
        return len(tails)
