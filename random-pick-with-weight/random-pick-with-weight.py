class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.index = [x for x in range(len(w))]

    def pickIndex(self) -> int:
        return random.choices(self.index, weights=self.w, k = 1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()