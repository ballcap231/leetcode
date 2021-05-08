from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #O(NlogN) time and O(1) space - Brute Force
        return sorted(s) == sorted(t)
        
        #O(N) time and O(1) space - hash table
        # return Counter(s) == Counter(t)
        
    