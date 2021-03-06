from heapq import heappush,heappushpop,heappop
class MedianFinder:
    #O(1) time and O(N) space
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_h = []
        self.max_h = []
        
    #O(logN) time and O(1) space
    def addNum(self, num: int) -> None:
        heappush(self.max_h, -heappushpop(self.min_h, num))
        if len(self.max_h) > len(self.min_h):
            heappush(self.min_h, -heappop(self.max_h))
    #O(1) time and O(1) space
    def findMedian(self) -> float:
        is_even = len(self.min_h) == len(self.max_h)
        
        if is_even:
            return (self.min_h[0] - self.max_h[0]) / 2
        else:
            return self.min_h[0]


#     #O(1) time and O(N) space
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.arr = []
        
#     #O(1) time and O(1) space
#     def addNum(self, num: int) -> None:
#         self.arr.append(num)
#     #O(NlogN) time and O(N) space
#     def findMedian(self) -> float:
#         self.arr.sort()
#         if self.arr and len(self.arr) % 2 == 0:
#             L,R = len(self.arr) // 2 - 1, len(self.arr) // 2
#             return (self.arr[L] + self.arr[R]) / 2
#         else:
#             return self.arr[len(self.arr) // 2]
    
    

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()