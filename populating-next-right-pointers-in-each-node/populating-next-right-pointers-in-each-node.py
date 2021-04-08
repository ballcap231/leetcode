"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #O(N) time and O(1) space
        #BFS without a queue, level order traversal as a linked list
        if root:
            curr_node = root
            first_node = root
            while first_node.left:
                first_node = first_node.left
                while curr_node:
                    curr_node.left.next = curr_node.right
                    if curr_node.next:
                        curr_node.right.next = curr_node.next.left
                    curr_node = curr_node.next
                curr_node = first_node
        return root
        
        
        
        #O(N) time and O(N) space - BFS
        # deq = deque()
        # if root: deq.append(root)
        # prev_node = None
        # while deq:
        #     for ii in range(len(deq)):
        #         curr_node = deq.popleft()
        #         if curr_node.left: deq.append(curr_node.left)
        #         if curr_node.right: deq.append(curr_node.right)
        #         if prev_node: prev_node.next = curr_node
        #         prev_node = curr_node
        #     curr_node.next = None
        #     prev_node = None
        # return root
        
        
    