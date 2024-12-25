# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]
        queue=deque([root])
        while queue:
            cntinlevel=len(queue)
            maxx=float('-inf')
            while cntinlevel:
                node=queue.popleft()
                maxx=max(maxx,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                cntinlevel-=1
            result.append(maxx)
        return result

        