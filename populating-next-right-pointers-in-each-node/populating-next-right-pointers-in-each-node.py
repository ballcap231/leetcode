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
        
        curr_node = root
        first_node = root
        while first_node:
            first_node = first_node.left
            while curr_node:
                if curr_node.left:
                    curr_node.left.next = curr_node.right
                if curr_node.right and curr_node.next:
                    curr_node.right.next = curr_node.next.left
                curr_node = curr_node.next
            curr_node = first_node
        
        return root
        
        
        
        
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
        
        
        
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        
        # Once we reach the final level, we are done
        while leftmost.left:
            
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                                                                                                                                             
                # Progress along the list (nodes on the current level)
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
        
        return root 