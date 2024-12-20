# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        store=[]
        queue=deque([(root,0)])
        temp=[]
        while queue:
            node,level=queue.popleft()
            if level&1:
                temp.append(node)
            if temp and level%2==0:
                start=0
                end=len(temp)-1
                while start<end:
                    temp[start].val,temp[end].val=temp[end].val,temp[start].val
                    start+=1
                    end-=1
                temp=[]
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        if temp:
            start=0
            end=len(temp)-1
            while start<end:
                temp[start].val,temp[end].val=temp[end].val,temp[start].val
                start+=1
                end-=1

        return root


        

        