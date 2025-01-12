# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxx=0
        def dfs(root):
            if not root:
                return -1
            lt,rt=0,0
            lt=1+dfs(root.left)
            rt=1+dfs(root.right)
            self.maxx=max(self.maxx,lt+rt)
            return max(lt,rt)
        dfs(root)
        return self.maxx
        