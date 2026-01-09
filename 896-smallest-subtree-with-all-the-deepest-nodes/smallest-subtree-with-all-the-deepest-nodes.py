# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth=-1
        count=0
        ans=None
        def recur(node,depth):
            nonlocal max_depth
            if depth>max_depth:
                max_depth=depth
            if node.left:
                recur(node.left,depth+1)
            if node.right:
                recur(node.right,depth+1)

        recur(root,1)


        def dfs(node,depth):
            nonlocal count
            nonlocal max_depth
            nonlocal ans
            if depth>max_depth:
                count=0
            if depth>=max_depth:
                ans=None
                count+=1
                max_depth=depth
            if depth==max_depth and not node.left and not node.right:
                temp=1
            else:
                temp=0
            if node.left:
                temp+=dfs(node.left,depth+1)
            if node.right:
                temp+=dfs(node.right,depth+1)
            print(node.val , temp,count,max_depth)
         
            if temp==count and not ans:
                ans=node
            
            return temp

        dfs(root,1)
        return ans if ans!=None else root
            

            
            
            

        