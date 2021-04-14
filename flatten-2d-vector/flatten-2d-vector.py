class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.arr = []
        self.curr_pos = 0
        for ls in vec:
            for num in ls:
                self.arr.append(num)
        
    def next(self) -> int:
        self.curr_pos += 1
        return self.arr[self.curr_pos - 1]
        
        
    def hasNext(self) -> bool:
        return self.curr_pos < len(self.arr)


# class Vector2D:

#     def __init__(self, vec: List[List[int]]):
#         self.vec = vec
#         self.curr_x = 0
#         self.curr_y = 0
#         self.curr_ls = vec[0] if vec else []
#         print(len(self.vec))
#         # [[[]]]
#         # [[]]
#         # [[[1,2],[3],[4]]] - [[[[1,2],[3],[4]]],[],[],[],[],[],[],[]]
#         # [[[],[3]]] - [[[[],[3]]],[],[],[]]
#     def next(self) -> int:
#         self.curr_ls = self.vec[self.curr_x]
#         to_ret = self.curr_ls[self.curr_y]
        
#         if self.curr_y + 1 >= len(self.curr_ls):
#             self.curr_y = 0
#             self.curr_x += 1
#         else:
#             self.curr_y += 1
#         return to_ret
        
#     def hasNext(self) -> bool:
#         if not self.vec or not self.vec[0]: return False
#         if self.curr_x == len(self.vec):
#             return False
#         return True


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()