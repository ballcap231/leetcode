# #Brute Force - O(N + V) initialization time and O(N) space
# #where N == number of ints, V == # of total lists in vec (including empty ones)
# class Vector2D:

#     def __init__(self, vec: List[List[int]]):#[[[],[3]]]
#         print(vec)
#         self.arr = []
#         self.curr_pos = 0
#         for ls in vec:
#             for num in ls:
#                 self.arr.append(num)
#         print(self.arr)
#     def next(self) -> int:
#         self.curr_pos += 1
#         return self.arr[self.curr_pos - 1]
        
        
#     def hasNext(self) -> bool:
#         return self.curr_pos < len(self.arr)
# ["Vector2D","hasNext","next","hasNext"]
# [[[[],[3]]],[],[],[]]


#O(V/N) time == O(N + V)/N == O(N/N + V/N) for next()
#O(1) time for hasNext()
#O(1) space for everything
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.curr_x = 0
        self.curr_y = -1
        self.curr_ls = vec[0] if vec else None
        self.find_next_num()
        
    def find_next_num(self):
        if self.curr_ls is None: return
        
        if self.curr_y + 1 >= len(self.curr_ls):
            self.curr_y = 0
            self.curr_x += 1
            while self.curr_x < len(self.vec) and not self.vec[self.curr_x]:
                self.curr_x += 1
        else:
            self.curr_y += 1
        
    def next(self) -> int:
        self.curr_ls = self.vec[self.curr_x]
        to_ret = self.curr_ls[self.curr_y]
        self.find_next_num()
        return to_ret
        
    def hasNext(self) -> bool:
        return self.curr_x < len(self.vec)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()