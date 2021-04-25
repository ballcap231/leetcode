class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #O(V) time where V == number of  vertices - would be O(V + E) but E == V - 1 since acyclic
        #O(V) space
        if n <= 2: return [xx for xx in range(n)]
        graph = defaultdict(set)
        
        for edge1, edge2 in edges:
            graph[edge1].add(edge2)
            graph[edge2].add(edge1)
            
        leaves = deque()
        for key, val in graph.items():
            if len(val) == 1:
                leaves.append(key)
        
        remain_leaves = n
        while remain_leaves > 2:
            remain_leaves -= len(leaves)
            new_leaves = deque()
            while leaves:
                curr_leaf = leaves.popleft()
                while graph[curr_leaf]:
                    nei = graph[curr_leaf].pop()
                    graph[nei].discard(curr_leaf)
                    if len(graph[nei]) == 1:
                        new_leaves.append(nei)
            leaves = new_leaves
        return leaves
                
            