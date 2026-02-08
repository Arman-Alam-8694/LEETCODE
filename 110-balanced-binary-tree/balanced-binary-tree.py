# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced=True
        def dfs(node):
            if not node:
                return 0
            ll=dfs(node.left)
            rr=dfs(node.right)
            if abs(ll-rr)>1:
                self.balanced=False
            return max(ll,rr)+1
           
      
        dfs(root)
        return self.balanced 
        