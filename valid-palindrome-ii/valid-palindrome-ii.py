class Solution:
    def validPalindrome(self, s: str) -> bool:
        #O(N) time and O(1) space
        diff_count = 0
        l,r = 0, len(s) - 1
        
        def valid_substring(l, r):
            while l < r:
                if s[l] != s[r]:
                    return l, r
                l += 1
                r -= 1
            return l, r
        l, r = valid_substring(l,r)
        if l < r:
            l_2, r_2 = valid_substring(l + 1, r)
            if l_2 < r_2:
                l_3, r_3 = valid_substring(l, r - 1)
        
        return l >= r or l_2 >= r_2 or l_3 >= r_3
            
                
        