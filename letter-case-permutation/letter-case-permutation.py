class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ret = []
        def backtrack(pos, string):
            if pos >= len(string):
                ret.append(string)
                return
            if not string[pos].isalpha():
                backtrack(pos + 1, string)
            else:
                backtrack(pos + 1, string[:pos] + string[pos].lower() + string[pos + 1:])
                backtrack(pos + 1, string[:pos] + string[pos].upper() + string[pos + 1:])
        
        backtrack(0, S)
        return ret
        
        
        # #O(2^N * N) time and space    
        # f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        # return map("".join, itertools.product(*map(f, S)))
    
#         self.ans = []
        
#         def backtrack(candidates, prev_combo):
#             for count, char in enumerate(candidates):
#                 for c in set((char, char.swapcase())):
#                     if len(prev_combo) + 1 == len(S):
#                         self.ans.append(prev_combo + c)
#                         continue
#                     backtrack(candidates[count + 1:], prev_combo + c)
                    
#         backtrack(S, "")
#         return self.ans
                