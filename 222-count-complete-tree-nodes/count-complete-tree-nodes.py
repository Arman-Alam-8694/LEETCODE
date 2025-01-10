# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal count
            if node.left:
                count+=1
                dfs(node.left)
            if node.right:
                count+=1
                dfs(node.right)
        count=1
        if not root:
            return 0
        dfs(root)
        return count