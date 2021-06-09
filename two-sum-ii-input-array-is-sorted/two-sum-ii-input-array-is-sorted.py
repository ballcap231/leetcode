class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #O(N) time and O(1) space
        low = 0
        high = len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1,high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1
        