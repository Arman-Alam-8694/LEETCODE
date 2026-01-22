class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0

        # 1. Simulate Doubly Linked List with arrays
        # next_idx[i] tells us who is the CURRENT valid neighbor to the right of i
        next_idx = [i + 1 for i in range(n)] 
        prev_idx = [i - 1 for i in range(n)]
        
        # We also need a 'valid' array to know if an index is still in the game
        valid = [True] * n 
        
        # 2. Count current inversions (how many pairs are unsorted)
        # We stop when this hits 0.
        inversion_count = 0
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                inversion_count += 1
                
        if inversion_count == 0:
            return 0

        # 3. Heap stores (sum, index) for ALL pairs
        # We use 'index' (the left element's index) for the tie-breaker
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i+1], i))

        ops = 0
        
        while inversion_count > 0:
            # Get the minimum sum pair
            current_sum, idx = heapq.heappop(heap)
            
            # --- LAZY DELETION CHECK ---
            # If 'idx' was removed, OR 'idx' no longer has a right neighbor, skip
            if not valid[idx] or next_idx[idx] >= n:
                continue
            
            right_neighbor = next_idx[idx]
            
            # Verify the sum is current (it might be an old entry in the heap)
            if nums[idx] + nums[right_neighbor] != current_sum:
                continue

            # --- PRE-MERGE: Remove old inversion counts ---
            # We are about to change nums[idx] and remove nums[right_neighbor].
            # We must undo their contribution to the 'inversion_count'.
            
            # Check left side: (prev_idx[idx], idx)
            left_neighbor = prev_idx[idx]
            if left_neighbor != -1:
                if nums[left_neighbor] > nums[idx]:
                    inversion_count -= 1
            
            # Check current pair: (idx, right_neighbor)
            if nums[idx] > nums[right_neighbor]:
                inversion_count -= 1
                
            # Check right side: (right_neighbor, next_of_right)
            next_of_right = next_idx[right_neighbor]
            if next_of_right < n:
                if nums[right_neighbor] > nums[next_of_right]:
                    inversion_count -= 1

            # --- MERGE OPERATION ---
            ops += 1
            # Update value at 'idx'
            nums[idx] = nums[idx] + nums[right_neighbor]
            
            # Remove 'right_neighbor' effectively
            valid[right_neighbor] = False
            
            # Update Pointers (The "Array Linked List" logic)
            # Link idx -> next_of_right
            next_idx[idx] = next_of_right
            # Link next_of_right -> idx
            if next_of_right < n:
                prev_idx[next_of_right] = idx
            
            # --- POST-MERGE: Add new inversion counts & push to heap ---
            
            # Check left side with NEW value
            if left_neighbor != -1:
                if nums[left_neighbor] > nums[idx]:
                    inversion_count += 1
                # Add new pair sum to heap
                heapq.heappush(heap, (nums[left_neighbor] + nums[idx], left_neighbor))
            
            # Check right side with NEW value (idx is now neighbor to next_of_right)
            if next_of_right < n:
                if nums[idx] > nums[next_of_right]:
                    inversion_count += 1
                # Add new pair sum to heap
                heapq.heappush(heap, (nums[idx] + nums[next_of_right], idx))
                
        return ops
        