from collections import OrderedDict
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.vals = dict()
        self.Q = OrderedDict()
        for val in nums:
            self.add(val)

    def showFirstUnique(self) -> int:
        if self.Q:
            return next(iter(self.Q))
        return -1
        # while self.Q:
        #     if self.vals[self.Q[0]] == 0:
        #         return self.Q[0]
        #     else:
        #         self.Q.popleft()
        # return -1

    def add(self, value: int) -> None:
        if value not in self.vals:
            self.vals[value] = 0
            self.Q[value] = 1
        else:
            self.vals[value] = -1
            if value in self.Q: del self.Q[value]
            


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)