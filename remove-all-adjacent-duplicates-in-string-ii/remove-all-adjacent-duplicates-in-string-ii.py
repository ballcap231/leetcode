class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #O(N) time and O(N) space
        k_counts = []
        temp_s = []
        for pos in range(len(s)):
            char = s[pos]
            if k_counts and temp_s and temp_s[-1] == char:
                k_counts.append(k_counts[-1] + 1)
            else:
                k_counts.append(1)

            temp_s.append(char)
            if k_counts[-1] == k:
                for _ in range(k):
                    k_counts.pop()
                    temp_s.pop()
            
            
        return ''.join(temp_s)
        
        
        
        
        
        
        # Stack with sliding window - better than brute force
#         stack = []
        
#         for pos in range(len(s)):
#             stack.append(s[pos])
#             if len(stack) >= k:
#                 for stack_pos in range(-1, -k, -1):
#                     if stack[stack_pos] != stack[stack_pos - 1]:
#                         break
#                 else:
#                     for _ in range(k):
#                         stack.pop()
#         return ''.join(stack)
        
        
        
        
        
        # #Brute Force - Sliding window
        # #O(|s|^2) time and O(|s|) space
        # temp_str = s
        # while True:
        #     l, r = 0, k
        #     while r <= len(temp_str):
        #         if len(set(temp_str[l:r])) == 1:
        #             temp_str = temp_str[:l] + temp_str[r:]
        #             break
        #         r += 1
        #         l += 1
        #     else:
        #         break
        # return temp_str