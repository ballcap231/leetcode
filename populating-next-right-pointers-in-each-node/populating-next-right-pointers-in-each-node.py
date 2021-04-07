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
        
        deq = deque()
        if root: deq.append(root)
        prev_node = None
        while deq:
            for ii in range(len(deq)):
                curr_node = deq.popleft()
                if curr_node.left: deq.append(curr_node.left)
                if curr_node.right: deq.append(curr_node.right)
                if prev_node: prev_node.next = curr_node
                prev_node = curr_node
            curr_node.next = None
            prev_node = None
        return root