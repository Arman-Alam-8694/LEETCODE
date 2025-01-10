# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node,count):
            if node is None:
                return 0
            count=1
            count+=dfs(node.left,count)
            count+=dfs(node.right,count)
            return count


        return dfs(root,0)