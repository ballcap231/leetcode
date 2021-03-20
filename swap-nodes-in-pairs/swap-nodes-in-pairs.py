# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, node: ListNode) -> ListNode:
        fake_head = ListNode(next = node)
        head = fake_head
        curr_node = node
        next_node = node.next if node else None

        def switch_nodes(head, node_l, node_r):
            node_l.next = node_r.next
            head.next = node_r
            node_r.next = node_l
            return node_l
        
        while curr_node and next_node:
            head = switch_nodes(head, curr_node, next_node)
            curr_node = head.next
            if curr_node:
                next_node = curr_node.next
        return fake_head.next
