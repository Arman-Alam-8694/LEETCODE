# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        stack=deque()
        stack.append((root,1))
        large=1
        lsum=float("-inf")
        prev=1
        summ=0
        while stack:
            node,level=stack.popleft()
            if prev!=level:
                if summ>lsum:
                    large=prev
                    lsum=summ
                prev=level
                summ=0
            summ+=node.val
            if node.left:
                stack.append((node.left,level+1))
            if node.right:
                stack.append((node.right,level+1))
        if summ>lsum:
            large=level
        return large
            
            

        