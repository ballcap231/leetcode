from collections import deque
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_ls = deque()
        l_arr = len(arr)
        max_val = -float('inf')
        first_pos = arr[-1]
        for xx in reversed(range(l_arr - 1)):
            max_val = max(first_pos,max_val)
            first_pos = arr[xx]
            new_ls.appendleft(max_val)
        
        new_ls.append(-1)
        return new_ls