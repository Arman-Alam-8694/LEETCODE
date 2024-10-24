# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        lookup=set()
        lookup2=set()
        if not root1 and not root2:
            return True
        if not root2 or not root1:
            return False
        
        
        stack=[root1]
        while stack:
            tstack=[]
            while stack:
                nodes=stack.pop()
                if nodes.right:
                    lookup.add((nodes.val,nodes.right.val))
                    tstack.append(nodes.right)
                if nodes.left:
                    lookup.add((nodes.val,nodes.left.val))
                    tstack.append(nodes.left)
            stack=tstack
        stack=[root2]
        while stack:
            tstack=[]
            while stack:
                nodes=stack.pop()
                if nodes.right:
                    lookup2.add((nodes.val,nodes.right.val))
                    tstack.append(nodes.right)
                if nodes.left:
                    lookup2.add((nodes.val,nodes.left.val))
                    tstack.append(nodes.left)
            stack=tstack
        if lookup==lookup2:
            return True
        return False
        


