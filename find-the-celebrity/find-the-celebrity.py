# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        #O(N) time and O(1) space
        #Sliding window of size 2 to check with of the 2 nodes COULD be the celebrity
        #Greedy approach
        
        candidate = 0
        for xx in range(1, n):
            if knows(candidate, xx):
                candidate = xx
        #The candidate node could be the celebrity OR there could be no celebrity
        #Greedy approach but no guarantees there is an answer...
        for xx in range(0,n):
            if xx != candidate:
                if knows(candidate, xx) or not knows(xx, candidate):
                    return -1
        return candidate