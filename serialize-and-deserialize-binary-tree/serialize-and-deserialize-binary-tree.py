# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.nodes = []
        def dfs(node):
            if node:
                self.nodes.append(node.val)
                dfs(node.left)
                dfs(node.right)
            else:
                self.nodes.append(10000000)

        dfs(root)
        return ','.join(map(str, self.nodes))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nums = list(map(int, data.split(',')))
        # return nums
        # return TreeNode(33)
        
        self.pos = 0
        def make_node():
            if nums[self.pos] == 10000000:
                return None
            new_node = TreeNode(nums[self.pos])
            return new_node
        def dfs():
            node = make_node()
            if node:
                self.pos += 1
                node.left = dfs()
                self.pos += 1
                node.right = dfs()
            return node
        
        return dfs()
        
        
#         self.curr_pos = 0
#         self.to_visit = [data[0]]
#         root = TreeNode()
#         while self.to_visit and self.curr_pos < len(data):
#             curr_node = self.to_visit.pop()
            
#             self.to_visit.append()
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))