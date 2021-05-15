class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            
            pivot_pos = random.randint(0, len(arr) - 1)
            pivot = arr[pivot_pos]
            mid, left, right = [], [], []
            
            for num in arr:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            left_arr = quick_sort(left)
            right_arr = quick_sort(right)
            
            return left_arr + mid + right_arr
        
        return quick_sort(nums)
            
        
        
        
#         def quick_sort(arr):
            
#             if len(arr) < 2:
#                 return arr
            
#             index = random.randint(0, len(arr) - 1)
#             L = [xx for xx in arr if xx < arr[index]]
#             M = [xx for xx in arr if xx == arr[index]]
#             R = [xx for xx in arr if xx > arr[index]]
            
            
#             return quick_sort(L) + M + quick_sort(R)
        
#         return quick_sort(nums)