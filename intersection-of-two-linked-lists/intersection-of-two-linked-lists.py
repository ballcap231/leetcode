# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #O(N + M) time where N and M are the lengths of the 2 lists
        #O(1) space
        #similar prob: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/submissions/
        pA = headA
        pB = headB
        
        while pA != pB:
            pA = pA.next if pA is not None else headB
            pB = pB.next if pB is not None else headA
        return pA
        
        
        
#         #O(|A| + |B|) time and O(1) space
#         curr_a, curr_b = headA, headB
#         a_passes, b_passes = 0, 0
        
#         while curr_a != curr_b:
#             if b_passes + a_passes > 2:
#                 return None
#             if curr_a.next:
#                 curr_a = curr_a.next
#             else:
#                 curr_a = headB
#                 a_passes += 1
#             if curr_b.next:
#                 curr_b = curr_b.next
#             else:
#                 curr_b = headA
#                 b_passes += 1
#         return curr_a
            
        
        
        
        
        
#         #O(N) time and O(N) space where N = |A| + |B|
#         nodes = set()
#         a_node = headA
#         b_node = headB
#         while a_node:
#             nodes.add(a_node)
#             a_node = a_node.next
        
#         while b_node:
#             if b_node in nodes: return b_node
#             b_node = b_node.next
        
#         return None