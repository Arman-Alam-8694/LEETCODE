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
        
        return stack[0] if stack else None