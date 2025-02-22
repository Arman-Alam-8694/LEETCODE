# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n=len(traversal)
        start=0
        temp=0
        while start<n and traversal[start]!="-" :
            temp*=10
            temp+=int(traversal[start])
            start+=1
        stack=[]
        cur_depth=0
        root=TreeNode(temp)
        stack.append(root)
        temp=0
        num_found=False
        for i in range(start,n):
            if traversal[i]=="-" and not num_found:
                cur_depth+=1
            elif traversal[i]!="-":
                if not num_found:
                    num_found=True
                temp*=10
                temp+=int(traversal[i])
            if (traversal[i]=="-" and num_found) or i==n-1:
                new_node=TreeNode(temp)
                temp=0
                while stack:
                    last_node=stack[-1]
                    if len(stack)==cur_depth:
                        if last_node.left is  None:
                            last_node.left=new_node
                            stack.append(new_node)
                        else:
                            last_node.right=new_node
                            stack.append(new_node)     
                        cur_depth=1
                        num_found=False
                        break
                    else:
                        stack.pop()
 
        return root


            


        