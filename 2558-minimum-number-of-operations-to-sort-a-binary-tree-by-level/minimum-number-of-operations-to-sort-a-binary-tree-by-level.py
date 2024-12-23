class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        # Minimum operations
        minOperations = 0
        
        # Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # To keep track of the index
            i = 0
            
            # List of values and their indices
            values = []
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Add to the list of values
                values.append([node.val, i])
                i += 1
                
                # If the node has a left child, push it to the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push it to the queue
                if node.right: queue.append(node.right)
                    
                # Update the count
                nodesInCurrentLevel -= 1
            print(values) 
            # Sorted list of indices based on the values
            sortedIndices = [i for val, i in sorted(values)]
            print(sortedIndices)
            
            # Calculate the minimum operations required
            # Here, we will use Swap Sort or Cycle Sort
            for i in range(len(sortedIndices)):
                
                # We need to make sure that a value "x" in "sortedIndices"
                # Is at the index "i"
                # If it is not, we need to place it at its correct place
                # And that will require one operation
                while sortedIndices[i] != i:
                    
                    # Swap
                    sortedIndices[sortedIndices[i]], sortedIndices[i] = sortedIndices[i], sortedIndices[sortedIndices[i]]
                    
                    # Upadate operation count
                    minOperations += 1
                    
                 
        # Return the minimum operations to sort each level
        return minOperations