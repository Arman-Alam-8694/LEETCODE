from typing import Optional

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        n = len(traversal)
        
        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            num = 0
            while i < n and traversal[i].isdigit():
                num = num * 10 + int(traversal[i])
                i += 1
            
            new_node = TreeNode(num)
            
            # Adjust the stack to the correct depth
            while len(stack) > depth:
                stack.pop()
            
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = new_node
                else:
                    stack[-1].right = new_node
            
            stack.append(new_node)
        
        #iterative for loop more complex implementation same tc and sc for both the solutions
        # n=len(traversal)
        # start=0
        # temp=0
        # while start<n and traversal[start]!="-" :
        #     temp*=10
        #     temp+=int(traversal[start])
        #     start+=1
        # stack=[]
        # cur_depth=0
        # root=TreeNode(temp)
        # stack.append(root)
        # temp=0
        # num_found=False
        # for i in range(start,n):
        #     if traversal[i]=="-" and not num_found:
        #         cur_depth+=1
        #     elif traversal[i]!="-":
        #         if not num_found:
        #             num_found=True
        #         temp*=10
        #         temp+=int(traversal[i])
        #     if (traversal[i]=="-" and num_found) or i==n-1:
        #         new_node=TreeNode(temp)
        #         temp=0
        #         while stack:
        #             last_node=stack[-1]
        #             if len(stack)==cur_depth:
        #                 if last_node.left is  None:
        #                     last_node.left=new_node
        #                     stack.append(new_node)
        #                 else:
        #                     last_node.right=new_node
        #                     stack.append(new_node)     
        #                 cur_depth=1
        #                 num_found=False
        #                 break
        #             else:
        #                 stack.pop()
 
        # return root
        return stack[0] if stack else None