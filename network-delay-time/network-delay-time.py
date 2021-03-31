from collections import deque
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Djikstra's Algorithm - 
        
#         graph = collections.defaultdict(list)
#         for u, v, w in times:
#             graph[u].append((v, w))

#         pq = [(0, k)]
#         dist = {}
#         while pq:
#             d, node = heapq.heappop(pq)
#             if node in dist: continue
#             dist[node] = d
#             for nei, d2 in graph[node]:
#                 if nei not in dist:
#                     heapq.heappush(pq, (d+d2, nei))

#         return max(dist.values()) if len(dist) == n else -1
        
        
        adj_list = defaultdict(list)
        for source, target, time in times:
            adj_list[source].append((target, time))
        
        fastest_time = {node: float('inf') for node in range(1, n + 1)}
        fastest_time[k] = 0
        max_time = 0
        seen = set()
        to_visit = [(0,k)]
        while to_visit:
            time_from_origin, node = heapq.heappop(to_visit)
            if node not in seen:
                seen.add(node)
                for neighbor, time in adj_list[node]:
                    if neighbor not in seen:
                        new_neighbor_time = min(fastest_time[neighbor], time_from_origin + time)
                        fastest_time[neighbor] = new_neighbor_time
                        if neighbor not in seen:
                            heapq.heappush(to_visit, (new_neighbor_time , neighbor))

                max_time = max(max_time, time_from_origin)
        
        max_time = max(fastest_time.values())
        return max_time if all((time != float('inf') for time in fastest_time.values())) else -1