from itertools import combinations
from collections import defaultdict, deque
class Solution:
    def is_mutation(self, gene1, gene2):
        diff = 0
        pos = 0
        while diff < 2 and pos < len(gene1):
            if gene1[pos] != gene2[pos]:
                diff += 1
            pos += 1
        return diff < 2
        
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        out_nodes = defaultdict(list)
        graph = bank + [start]
        combos = combinations(graph, r = 2)
        
        for combo in combos:
            if self.is_mutation(combo[0], combo[1]):
                out_nodes[combo[0]].append(combo[1])
                out_nodes[combo[1]].append(combo[0])
        
        if end not in out_nodes: return -1
        
        dq = deque([(start, 0)])
        visited = set([start])
        # BFS
        
        while dq:
            curr_node, depth = dq.popleft()
            for node in out_nodes[curr_node]:
                if node == end:
                    return depth + 1
                if node not in visited:
                    visited.add(node)
                    dq.append((node, depth + 1))
                    
        return -1
            
            
        
        
        