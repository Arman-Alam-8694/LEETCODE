# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxx=float('-inf')
        def dfs(root):
            if not root:
                return 0
            lt=dfs(root.left)
            rt=dfs(root.right)
            self.maxx=max(self.maxx,rt+lt+root.val,root.val,root.val+lt,root.val+rt)
            return max(root.val,root.val+lt,root.val+rt)
        dfs(root)
        return self.maxx


        