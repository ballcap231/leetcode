# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        inorder_index = {}
        
        for pos, val in enumerate(inorder):
            inorder_index[val] = pos
        self.preorder_pos = 0
        
        def construct_tree(left, right):
            if left > right:
                return None
            
            new_root = preorder[self.preorder_pos]
            node = TreeNode(new_root)
            self.preorder_pos += 1
            
            inorder_pos = inorder_index[new_root]
            
            node.left = construct_tree(left, inorder_pos - 1)
            node.right = construct_tree(inorder_pos + 1, right)
            
            return node
        
        return construct_tree(0, len(preorder) - 1)
        
        
        
        
        
        
#         def array_to_tree(left, right):
#             nonlocal preorder_index
#             # if there are no elements to construct the tree
#             if left > right: return None

#             # select the preorder_index element as the root and increment it
#             root_value = preorder[preorder_index]
#             root = TreeNode(root_value)


#             preorder_index += 1

#             # build left and right subtree
#             # excluding inorder_index_map[root_value] element because it's the root
#             root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
#             root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

#             return root

#         preorder_index = 0

#         # build a hashmap to store value -> its index relations
#         inorder_index_map = {}
#         for index, value in enumerate(inorder):
#             inorder_index_map[value] = index

#         return array_to_tree(0, len(preorder) - 1)