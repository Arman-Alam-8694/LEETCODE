# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sum=[]
        if not root:
            return -1
        stack=[root]
        level=1
        while stack:
            temp=0
            tstack=[]
            while stack:
                node=stack.pop()
                temp+=node.val
                if node.left:
                    tstack.append(node.left)
                if node.right:
                    tstack.append(node.right)
            level_sum.append(temp)
            stack=tstack
            level+=1
        if k>len(level_sum):
            return -1
        level_sum.sort()
        print(level_sum)
        return level_sum[-k]
