class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        dq = deque()
        for bt in sorted(boxTypes, key = lambda x : x[1], reverse=True):
            dq.append(bt)
        
        ret = 0
        
        while truckSize > 0 and dq:
            dq[0][0] -= 1
            units = dq[0][1]
            if dq[0][0] == 0:
                dq.popleft()
            ret += units
            truckSize -= 1
        
        return ret
        
        