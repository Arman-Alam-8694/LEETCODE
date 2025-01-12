# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.answer=True
        def dfs(root):
            if not root:
                return 0
            lt,rt=0,0
            lt=1+dfs(root.left)
            rt=1+dfs(root.right)
            if abs(rt-lt)>1:
                self.answer=False
            return max(lt,rt)
        dfs(root)
        return self.answer