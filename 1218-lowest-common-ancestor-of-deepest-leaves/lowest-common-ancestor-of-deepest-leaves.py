# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node,height):
            if not node:
                return None,height
            
            left,lheight=dfs(node.left,height+1)
            
            right,rheight=dfs(node.right,height+1)
            if lheight==rheight:
                return node,lheight
            if lheight>rheight:
                return left,lheight
            else:
                return right,rheight

        lca,height=dfs(root,1)
        return lca
            
            
        