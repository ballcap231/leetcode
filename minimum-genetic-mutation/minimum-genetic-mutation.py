from itertools import combinations
from collections import defaultdict, deque
class Solution:
    def is_mutation(self, gene1, gene2):
        #Returns if Hamming Distance is less than 2
        diff = 0
        pos = 0
        while diff < 2 and pos < len(gene1):
            if gene1[pos] != gene2[pos]:
                diff += 1
            pos += 1
        return diff < 2
        
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        #O(V^2 + V + E) == O(V^2) time and O(V^2) space, 
        # where V = |bank| and E = number of genes pairs that differs by 1 char in bank
        # but V^2 is always larger than E since V^2 is all gene pairs possible in bank
        out_nodes = defaultdict(list)
        graph = bank + [start]
        #Takes O(V^2) time and space to build all possible gene pair combinations
        combos = combinations(graph, r = 2)
        
        for combo in combos:
            if self.is_mutation(combo[0], combo[1]):
                out_nodes[combo[0]].append(combo[1])
                out_nodes[combo[1]].append(combo[0])

        dq = deque([(start, 0)])
        visited = set([start])
        # BFS - takes O(V + E) traversal and O(V) space
        while dq:
            curr_node, depth = dq.popleft()
            for node in out_nodes[curr_node]:
                if node == end:
                    return depth + 1
                if node not in visited:
                    visited.add(node)
                    dq.append((node, depth + 1))
                    
        return -1
            
            
        
        
        