class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        import heapq

        # Minimum operations counter
        minOperations = 0
        
        # BFS for level order traversal
        queue = deque([root])
        
        while queue:
            # Collect values at the current level
            level_size = len(queue)
            values = []
            
            for i in range(level_size):
                node = queue.popleft()
                if node:  # Only include non-null nodes
                    values.append([-node.val, i])  # Negative for max-heap simulation
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if len(values) == 0:
                continue
            
            # Create a copy of the original order
            original = values[:]
            
            # Build a min-heap for sorting
            heapq.heapify(values)
            last = len(values) - 1
            
            # Set to track already swapped nodes
            swapped = set()
            
            # Sorting logic using heap
            while last > 0 :
              
            
                val, idx = heapq.heappop(values)
                
                if (val, idx) in swapped:
                   
                    continue
                
                pval, pidx = original[last]
                
                if idx == last:
                    last -= 1
                else:
                    swapped.add((pval, last))
                    original[idx], original[last] = original[last], original[idx]
                    heapq.heappush(values, [pval, idx])
                    minOperations += 1
                    last-=1
                # print(minOperations)
                # print(original)
        
        return minOperations
