"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        #O(N) time and O(1) space
        n_1, n_2 = p,q
        
        while n_1 != n_2:
            n_1 = n_1.parent if n_1.parent else q
            n_2 = n_2.parent if n_2.parent else p
        
        return n_1
        
        # p1, q1 = p, q
        # while p1 != q1:
        #     p1 = p1.parent if p1.parent else q
        #     q1 = q1.parent if q1.parent else p
        # return p1
    
#         p_parents = []
#         q_parents = set()
        
#         def add_to_parent(node,parents):
#             if isinstance(parents, list): 
#                 parents.append(node)
#             else:
#                 parents.add(node)
        
#         def get_parents(node,parents):
#             add_to_parent(node,parents)
#             while node.parent:
#                 add_to_parent(node.parent, parents)
#                 node = node.parent
        
#         get_parents(p,p_parents)
#         get_parents(q,q_parents)
        
#         for ii in p_parents:
#             if ii in q_parents:
#                 return ii
        
        
            
                