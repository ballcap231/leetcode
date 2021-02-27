class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        #O(N) time and O(1) space
        #Greedy
        last_chars = {}
        for pos, char in enumerate(S):
            last_chars[char] = pos
    
        anchor = max_partition_size = 0
        partitions = []
        for pos, char in enumerate(S):
            max_partition_size = max(max_partition_size, last_chars[char])
            if max_partition_size == pos:
                partitions.append(pos - anchor + 1)
                anchor = pos + 1
        return partitions
        
        