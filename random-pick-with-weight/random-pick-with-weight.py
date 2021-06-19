# prefix sum using binary search
class Solution:
    #O(N) time and space
    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sum = [0]
        curr_sum = 0
        for val in w:
            curr_sum += val
            self.prefix_sum.append(curr_sum)
            
    #O(logN) time and O(1) space
    def pickIndex(self) -> int:
        randint = random.randint(1, self.prefix_sum[-1])
        L,R = 0, len(self.prefix_sum) - 1

        while L < R:
            M = (L + R) // 2
            if self.prefix_sum[M] < randint <= self.prefix_sum[M + 1]:
                return M
            elif self.prefix_sum[M + 1] < randint:
                L = M + 1
            else:
                R = M



# #Brute force using prefix sum with linear scan
# class Solution:
#     #O(N) time and space
#     def __init__(self, w: List[int]):
#         self.w = w
#         self.index = [0]
#         self.sum = 0
#         for ii in w:
#             self.sum += ii
#             self.index.append(self.sum)
#     #O(N) time and O(1) space
#     def pickIndex(self) -> int:
#         randint = random.randint(1, self.index[-1])
#         for pos in range(len(self.index) - 1):
#             if self.index[pos] < randint <= self.index[pos + 1]:
#                 return pos


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()





# class Solution:

#     def __init__(self, w: List[int]):
#         self.w = w
#         self.index = [x for x in range(len(w))]

#     def pickIndex(self) -> int:
#         return random.choices(self.index, weights=self.w, k = 1)[0]


# # Your Solution object will be instantiated and called as such:
# # obj = Solution(w)
# # param_1 = obj.pickIndex()