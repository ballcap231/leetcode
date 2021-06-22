class Solution(object):
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {len(s):['']}

        def loop(i):
            if i not in memo:
                temp = []
                for j in range(i+1,len(s)+1):
                    if s[i:j] in wordDict:
                        for tail in loop(j):
                            temp.append(s[i:j] + (tail and ' ' + tail))
                memo[i] = temp
            return memo[i]
        return loop(0)