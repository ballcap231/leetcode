class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #Backtracking solution
        #O(N * 2^N) - very loose time and space bound
        #O(N) time if output list is not part of space complexity - comes from curr_arr
        #Same complexity analysis as that for a superset of nodes
        #https://leetcode.com/problems/subsets/
        #Because there are 2^N possible sets (each element is in or not in a set)
        #In each set, there is a possibility of up to N elements or N nodes
        ret = []
        curr_arr = []
        target = len(graph) - 1
        def backtrack(node):
            if node == target:
                return True
            curr_arr.append(node)
            for child_node in graph[node]:
                if backtrack(child_node):
                    ret.append(curr_arr + [target])
            curr_arr.pop()
            return False
        backtrack(0)
        return ret
        
        
        
#         #DP solution - O(N * 2^N) time and space
#         @lru_cache(maxsize=None)
#         def track(node):
#             if node == len(graph) - 1:
#                 return [[node]]
#             ret = []
#             for child_node in graph[node]:
#                 for paths in track(child_node):
#                     if paths:
#                         ret.append([node] + paths)
#             return ret

#         return track(0)