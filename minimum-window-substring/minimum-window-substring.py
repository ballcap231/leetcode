class Solution:
    def valid_substr(self):
        return all(self.curr_counts.get(key, -1) >= val for key,val in self.t_counts.items())
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''
        self.t_counts = Counter(t)
        self.curr_counts = Counter()
        L = R = 0
        min_len = float("inf")
        min_L = min_R = None
        
        while R < len(s):
            self.curr_counts[s[R]] += 1
            while self.valid_substr():
                if R + 1 - L < min_len:
                    min_len = R + 1 - L
                    min_L, min_R = L, R + 1
                self.curr_counts[s[L]] -= 1
                L += 1
            R += 1
        
        return s[min_L:min_R] if min_len != float("inf") else ""
        