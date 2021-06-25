class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for pos in range(len(s)):
            if stack and stack[-1] == s[pos]:
                stack.pop()
            else:
                stack.append(s[pos])
        return ''.join(stack)
        
        
        
        
        
        
        
        #Removing 2 or more adjacent letters:        
#         #O(N) time and O(N) space
#         stack = []
        
#         for pos in range(len(s)):
#             char = s[pos]
            
#             if stack and stack[-1] == char and (pos + 1 == len(s) or s[pos + 1] != s[pos]):
#                 while stack and stack[-1] == char:
#                     stack.pop()
#             else:
#                 stack.append(char)
#         return ''.join(stack)
                
        