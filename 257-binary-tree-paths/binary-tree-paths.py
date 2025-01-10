# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def recur(root,path):
            if not root:
                return 
            path.append(str(root.val))
            if not root.left and not root.right:
                result.append("->".join(path))
               
            else:
                recur(root.left,path)
                recur(root.right,path)
            path.pop()
           
        result=[]
        recur(root,[])
        return result
        