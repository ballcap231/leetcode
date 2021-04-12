class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        if not needle: return 0
        if needle not in haystack: return -1

        def partial(pattern):
            """ Calculate partial match table: String -> [Int]"""
            ret = [0]

            for i in range(1, len(pattern)):
                j = ret[i - 1]
                while j > 0 and pattern[j] != pattern[i]:
                    j = ret[j - 1]
                ret.append(j + 1 if pattern[j] == pattern[i] else j)
            return ret

            
        match_table = partial(needle)
        
        haystack_p = needle_p = 0
        print(match_table)
        while haystack_p < len(haystack):
            if haystack[haystack_p] == needle[needle_p]:
                haystack_p += 1
                needle_p += 1
                print(needle_p, haystack_p, )
                if needle_p == len(needle):
                    return haystack_p - needle_p
            else:
                if needle_p == 0:
                    haystack_p += 1
                else:
                    needle_p = match_table[needle_p - 1]
            
        