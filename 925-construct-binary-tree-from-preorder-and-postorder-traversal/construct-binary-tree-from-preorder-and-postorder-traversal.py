# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        
        def construct(prelist, postlist):
            if not prelist or not postlist:
                return None
            
            node = TreeNode(prelist[0])  # Root node
            
            if len(prelist) == 1:  # Base case: Single node tree
                return node
            
            # Find left subtree size
            left_end = 1  # Left subtree starts at index 1
            for i in range(1, len(prelist)):
                if prelist[i] == postlist[-2]:  # Second last element in postorder is the root of right subtree
                    left_end = i
                    break

            # Recursively construct left and right subtrees
            node.left = construct(prelist[1:left_end], postlist[:left_end-1])  # Left subtree
            node.right = construct(prelist[left_end:], postlist[left_end-1:-1])  # Right subtree

            return node

        return construct(preorder, postorder)
