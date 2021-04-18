class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        #O(N) time or O(max_unique * |s|) or O(26 * |s|)
        #O(1) space
        if k > len(s): return 0
        char_counts = Counter(s)
        max_unique = len(char_counts)
        longest_str = 0
        self.k = k
        
        for unique_count in range(1,max_unique + 1):
            L,R = -1,0
            self.reset_char_counters()
            while R < len(s):
                self.curr_char_counts[s[R]] += 1 
                self.update_valid_chars(s[R])
                while len(self.curr_char_counts) > unique_count:
                    L += 1
                    self.curr_char_counts[s[L]] -= 1
                    if self.curr_char_counts[s[L]] == 0:
                        self.curr_char_counts.pop(s[L])
                    self.update_valid_chars(s[L])
                if len(self.valid_chars) == len(self.curr_char_counts):
                    longest_str = max(longest_str, R - L)
                R += 1
        return longest_str
    
    def reset_char_counters(self):
        self.curr_char_counts = Counter()
        self.valid_chars = set()
    def update_valid_chars(self, char):
        if self.curr_char_counts[char] >= self.k:
            self.valid_chars.add(char)
        else:
            self.valid_chars.discard(char)
            
        
        