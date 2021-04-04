# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set()
        a_node = headA
        b_node = headB
        while a_node:
            nodes.add(a_node)
            a_node = a_node.next
        
        while b_node:
            if b_node in nodes: return b_node
            b_node = b_node.next
        
        return None