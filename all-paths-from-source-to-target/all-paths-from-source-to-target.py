class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #DP solution - O(N * 2^N) time and space
        @lru_cache(maxsize=None)
        def track(node):
            if node == len(graph) - 1:
                return [[node]]
            ret = []
            for child_node in graph[node]:
                for paths in track(child_node):
                    if paths:
                        ret.append([node] + paths)
            return ret

        return track(0)