# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            ll,rr=0,0
            if node.left:
                yes,lval=dfs(node.left)
                if not yes:
                    return False,lval
                ll=1+lval
            if node.right:
                ryes,rval=dfs(node.right)
                if not ryes:
                    return False,rval
                rr=1+rval
            temp=max(ll,rr)
            if abs(ll-rr)>1:
                return False,temp
            else:
                return True,temp   
        if not root:
            return True
        res,val=dfs(root)
        return res             
        