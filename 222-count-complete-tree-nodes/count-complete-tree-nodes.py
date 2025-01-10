# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def recur(node):
            if not node:
                return 0
            lh=dfsleft(node)
            rh=dfsright(node)
            if lh==rh:
                return 2**lh-1
            return 1+recur(node.left)+recur(node.right)


        def dfsleft(node):
            count=1
            while node.left:
                count+=1
                node=node.left
            return count
        

        def dfsright(node):
            count=1
            while node.right:
                count+=1
                node=node.right
            return count

        return recur(root)