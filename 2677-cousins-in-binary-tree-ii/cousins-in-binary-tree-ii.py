# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        cousins=[0]
        stack=[root]
        parents=[[0]]
        while stack:
            tempstack=[]
            tempsum=0
            p=[]
            while stack:
                parent=stack.pop()
                p.append(parent)
                if parent.left:
                    left_child=parent.left
                    tempstack.append(left_child)
                    tempsum+=parent.left.val
                
                if parent.right:
                    right_child=parent.right
                    tempstack.append(right_child)
                    tempsum+=parent.right.val
                   
            cousins.append(tempsum)
            stack=tempstack
        print(cousins)
        
        nstack=[(root,root.val)]
        root.val=0
        level=1
        while nstack:
            tempstack=[]
            while nstack:
                parent,prev=nstack.pop()
                if level>=len(cousins):
                    break
                total_sum=cousins[level]
                # print(iterate)
                if parent.left:
                    total_sum-=parent.left.val
                if parent.right:
                    total_sum-=parent.right.val

                if parent.left:
                    tempstack.append((parent.left,parent.left.val))
                    parent.left.val=total_sum

                 
                if parent.right:
                    tempstack.append((parent.right,parent.right.val))
                    parent.right.val=total_sum
            level+=1
            nstack=tempstack
        return root

        