from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        output = []
        for pos, word in enumerate(strs):
            counter = Counter(sorted(word))
            key = tuple(counter.items())
            dd[key].append(pos)
        print(dd)
        for key,val in dd.items():
            new_ls = []
            for ii in val:
                new_ls.append(strs[ii])
            output.append(new_ls)
        return output
        
        
        
        
        # dd = defaultdict(list)
        # for s in strs:
        #     dd2 = defaultdict(int)
        #     for c in s:
        #         dd2[c] += 1
        #     dd[frozenset(dd2.items())].append(s)
        # return dd.values()