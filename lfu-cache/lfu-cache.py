class LFUCache:

    def __init__(self, capacity: int):
        self.key_freq = {}
        self.freq_key = defaultdict(OrderedDict)
        self.min_freq = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key_freq:
            return -1
        kf = self.key_freq[key]
        self.key_freq[key] += 1
        val = self.freq_key[kf].pop(key)
        self.freq_key[kf + 1][key] = val
        if not self.freq_key[kf]:
            if kf == self.min_freq:
                self.min_freq += 1
            del self.freq_key[kf]
        
        return val
        

    def put(self, key: int, value: int) -> None:
        #already at capacity
        #not at capacity yet
        #putting a value that is already in the cache
        if self.capacity <= 0:
            return
        if key in self.key_freq:
            fq = self.key_freq[key]
            self.freq_key[fq][key] = value
            self.get(key)
            return
        if len(self.key_freq) == self.capacity:
            delK, delV = self.freq_key[self.min_freq].popitem(last=False)
            self.key_freq.pop(delK)
        self.key_freq[key] = 1
        self.freq_key[1][key] = value
        self.min_freq = 1
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)