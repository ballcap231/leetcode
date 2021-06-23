class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
#         #Sliding window - brute force
#         #O(N) time and O(1) space
#         curr_sum = 0
#         count = 0
#         l = 1
#         for r in range(1, n + 1):
#             curr_sum += r
            
#             while curr_sum > n:
#                 curr_sum -= l
#                 l += 1
            
#             if curr_sum == n:
#                 count += 1
#         return count
        
        #Math - O(N ** 0.5) time and O(1) space
        count = 0
        count2 = 0
        upper_bound = ceil((2 * n + 0.25) ** 0.5 - 0.5)
        for k in range(1, upper_bound + 1):
            x = n / k -  (k + 1) / 2
            if int(x) == x:
                count += 1
            if (n - k * (k + 1) // 2) % k == 0:
                count2 += 1
                print(x, (n - k * (k + 1) // 2), count, count2)
        
        return count2