from collections import defaultdict, deque
class Node:
    def __init__(self):
        self.indegrees = 0
        self.out_nodes = []
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(Node)
        tot_dep = 0
        for next_course, prev_course in prerequisites:
            graph[next_course].indegrees += 1
            graph[prev_course].out_nodes.append(next_course)
            tot_dep += 1
        
        no_dep = []
        for node in graph:
            if graph[node].indegrees == 0:
                no_dep.append(node)
        
        removed_edges = 0
        to_take = deque()
        all_courses = set(xx for xx in range(numCourses))
        while no_dep:
            curr_course = no_dep.pop()
            to_take.append(curr_course)
            all_courses.remove(curr_course)
            for out in graph[curr_course].out_nodes:
                graph[out].indegrees -= 1
                removed_edges += 1
                if graph[out].indegrees == 0:
                    no_dep.append(out)
        if removed_edges == tot_dep:
            for course in all_courses:
                to_take.appendleft(course)
            return to_take
        else:
            return []
        