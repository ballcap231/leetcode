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
    
    
#Explanation behind solution above:  
# This is so simple it seems stupid...

# For anyone struggling to see it, imagine to nodes, p and q, whose paths merge and become common after a certain number of steps.
# p1 -> p2 -> p3 -> c1 -> c2 -> c3
# q1 -> q2 -> q3 -> c1 -> c2 -> c3
# If the distance from p1 to c1 is the same as the distance from q1 to c1, it's pretty obvious this algorithm will find when c1 == c1.

# But now imagine those distances are different.
# p1 -> p2 -> p3 -> c1 -> c2 -> c3
# .........................q1 -> c1 -> c2 -> c3

# If you force them to switch paths after they reach c3:
# P Travels: (3 steps to c1), (3 common steps to q1), (1 step to c1)
# Q Travels: (1 step to c1), (3 common steps to p1), (3 steps to c1)

# OR put another way

# P Travels: PC, C, QC
# Q Travels: QC, C, PC

# where C is the common paths. PC is p's unique path to the common ancestor. QC is q's unique path.

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
        
        
            
                