class LargerNumKey(str):
    def __lt__(x, y):
        #O(K) solution where K is the longest string in nums 
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # #O(N * K * logN) time and O(N) space where N = len(nums)
        # largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        # return '0' if largest_num[0] == '0' else largest_num
        
        #O(N * K * logN) time and O(N) space where N = len(nums)
        #and where K is the longest string in nums 
        self.str_nums = [str(num) for num in nums]
        def l_greater_than_r(l,r):
            l_str = l + r
            r_str = r + l
            if l_str > r_str:
                return 1
            elif l_str < r_str:
                return -1
            else:
                return 0
        
        def quicksort(arr):
            if len(arr) < 2:
                return arr
            
            pivot = random.randint(0, len(arr) - 1)
            l, m, r = [], [], []
            
            for pos in range(len(arr)):
                compare_val = l_greater_than_r(arr[pos],arr[pivot])
                if compare_val == 1:
                    l.append(arr[pos])
                elif compare_val == -1:
                    r.append(arr[pos])
                else:
                    m.append(arr[pos])
            
            l_arr = quicksort(l)
            r_arr = quicksort(r)
            
            return l_arr + m + r_arr
        
        sorted_nums = quicksort(self.str_nums)
        
        ret_str = ''.join(sorted_nums)
        return ret_str if ret_str[0] != '0' else '0'
    
        
        
        
            
            