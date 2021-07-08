from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        output = []
        for pos, word in enumerate(strs):
            counter = Counter(word)
            # key = tuple(sorted(counter.items()))
            key = frozenset(counter.items())
            dd[key].append(pos)
        for key,val in dd.items():
            new_ls = []
            for ii in val:
                new_ls.append(strs[ii])
            output.append(new_ls)
        return output
        
        
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     ans[tuple(count)].append(s)
        # return ans.values()        
        

        
        # dd = defaultdict(list)
        # for s in strs:
        #     dd2 = defaultdict(int)
        #     for c in s:
        #         dd2[c] += 1
        #     dd[frozenset(dd2.items())].append(s)
        # return dd.values()