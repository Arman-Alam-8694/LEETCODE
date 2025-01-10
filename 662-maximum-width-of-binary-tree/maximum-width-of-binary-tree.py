from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = deque([(1, root)])  # Start with root node at index 1
        max_width = 1  # Initialize max width to 1

        while stack:
            level_length = len(stack)
            left = stack[0][0]  # Index of the first node at this level
            right = stack[-1][0]  # Index of the last node at this level

            max_width = max(max_width, right - left + 1)  # Update max width
            
            # Prepare the next level of nodes
            for _ in range(level_length):
                idx, node = stack.popleft()

                # Add left child to stack (if exists)
                if node.left:
                    stack.append((2 *idx, node.left))

                # Add right child to stack (if exists)
                if node.right:
                    stack.append((2 *idx+1, node.right))

        return max_width
