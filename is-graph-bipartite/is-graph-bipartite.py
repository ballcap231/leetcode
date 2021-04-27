class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #O(V + E) time and O(V) space
        colors = {}
        dq = deque()
        for curr_node in range(len(graph)):
            if curr_node not in colors:
                dq.append(curr_node)
                colors[curr_node] = 0
                while dq:
                    node = dq.popleft()
                    for nei in graph[node]:
                        if nei not in colors:
                            colors[nei] = colors[node] ^ 1
                            dq.append(nei)
                        elif colors[nei] == colors[node]:
                            return False
        return True
                            
                        
                            
                        