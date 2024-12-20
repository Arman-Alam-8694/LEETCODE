# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        storee={}
        store=[]
        queue=deque([(root,0)])
        temp=deque()
        curr=None
        while queue:
            node,level=queue.popleft()
            if level&1:
                if curr!=None and level!=curr:
                    storee[curr]=temp
                    store.append(temp)
                    temp=deque()
                curr=level
            if curr!=None and (level&1 and curr&1):
                temp.appendleft(node.val)
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        if temp:
            store.append(temp)
            storee[curr]=temp
        store=deque(store)
     
        queue=deque([(root,0)])
        curr=None
        while queue:
            node,level=queue.popleft()
            if level&1:
                if curr!=None and level!=curr:
                    store.popleft()
                curr=level
            if curr!=None and (level&1 and curr&1):
                node.val=store[0].popleft()
            
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))

        
        return root


        

        