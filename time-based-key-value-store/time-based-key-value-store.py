class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key].append((-1, ""))
        self.map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        
        times = self.map[key]
        times.append((float('inf'), ""))
        L,R = 0,len(times) - 1
        while L < R:
            M = (L + R) // 2
            if times[M][0] <= timestamp < times[M + 1][0]:
                times.pop()
                return times[M][1]
            if timestamp > times[M][0]:
                L = M + 1
            else:
                R = M
        times.pop()
        return times[L][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)