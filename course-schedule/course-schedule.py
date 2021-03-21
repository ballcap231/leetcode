from collections import defaultdict
class node:
    def __init__(self):
        self.indegrees = 0
        self.out_node_vals = []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(node)
        tot_dep = 0
        for prereq in prerequisites:
            next_course, prev_course = prereq[0], prereq[1]
            graph[next_course].indegrees += 1
            graph[prev_course].out_node_vals.append(next_course)
            tot_dep += 1
        
        no_dep_nodes = []
        for node_val in graph:
            if graph[node_val].indegrees == 0:
                no_dep_nodes.append(node_val)
                
        removed_edges = 0
        while no_dep_nodes:
            node_val = no_dep_nodes.pop()
            for out_node_val in graph[node_val].out_node_vals:
                graph[out_node_val].indegrees -= 1
                if graph[out_node_val].indegrees == 0:
                    no_dep_nodes.append(out_node_val)
                removed_edges += 1
        return tot_dep == removed_edges
    
    
    
    
    
# class node:
#     def __init__(self):
#         self.indegrees = 0
#         self.out_nodes = []

# def topological_sort(edges):
#     #edges: list(list[int]) -> [[1,0],[3,1] -> 0 points to 1, and 2 points to 3
    
    