class Solution:
    def reorganizeString(self, S: str) -> str:
        #Brute force using backtracking - exponential complexity
#         char_counts = Counter(S)
        
#         def test_char(prev_chars, counts):
#             if not counts:
#                 return prev_chars    
#             for char, num_left in list(counts.items()):
#                 if not prev_chars or prev_chars[-1] != char:
#                     counts[char] -= 1
#                     if counts[char] == 0:
#                         counts.pop(char)
#                     ret = test_char(prev_chars + [char],counts)
#                     counts[char] += 1
#                     if ret:
#                         return ret
#             return ""
#         return "".join(list(test_char([],char_counts)))

        
        #O(|S|) time complexity and O(1) space - since only 26 letters in alphabet
        counts = Counter(S)
        max_freq = counts.most_common(1)[0][1]
        #Only way a solution wouldn't be possible is if one char
        #has more chars than twice total chars
        if max_freq * 2 > len(S) + 1:
            return ""
        
        hq = []
        for key, val in counts.items():
            heapq.heappush(hq, (-val, key))
        ans = []
        while hq:
            neg_count, char = heapq.heappop(hq)
            if not ans or ans[-1] != char:
                ans.append(char)
                if neg_count != -1:
                    heapq.heappush(hq, (neg_count + 1, char))
            else:
                neg_count2,char2 = heapq.heappop(hq)
                ans.append(char2)
                heapq.heappush(hq,(neg_count, char))
                if neg_count2 != -1:
                    heapq.heappush(hq, (neg_count2 + 1, char2))

        return "".join(ans)
        
    