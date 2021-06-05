class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        table = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
        
        
        for pos1 in range(len(text1)):
            for pos2 in range(len(text2)):
                if text1[pos1] == text2[pos2]:
                    table[pos2 + 1][pos1 + 1] = table[pos2][pos1] + 1
                else:
                    table[pos2 + 1][pos1 + 1] = max(table[pos2][pos1 + 1], table[pos2 + 1][pos1])
        
        return table[-1][-1]