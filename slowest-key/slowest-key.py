class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        #O(N) time and O(1) space
        slowest_key = keysPressed[0]
        slowest_time = releaseTimes[0]
        for prev_pos, time in enumerate(releaseTimes[1:]):
            duration = time - releaseTimes[prev_pos]
            if duration > slowest_time or \
                (duration == slowest_time and keysPressed[prev_pos + 1] > slowest_key):
                slowest_key = keysPressed[prev_pos + 1]
                slowest_time = duration
        return slowest_key