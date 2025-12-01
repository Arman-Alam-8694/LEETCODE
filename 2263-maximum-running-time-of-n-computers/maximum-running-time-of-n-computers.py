class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        
        total_len = len(batteries)
        
        # 1. Pointers Setup
        # The Consumers start at index (total_len - n)
        consumer_start_index = total_len - n
        
        # The Stack ends at index (total_len - n - 1)
        stack_ptr = consumer_start_index - 1
        
        # Variable to hold loose energy we grabbed from the stack pointer
        current_spare_energy = 0
        
        # 2. Iterate through the consumers (Sorted Array replaces the Heap)
        # We stop before the last element because we always peek at i+1
        for i in range(consumer_start_index, total_len - 1):
            
            current_val = batteries[i]
            next_val = batteries[i+1]
            
            # DISTINCT LOGIC:
            # If current and next are same, we just continue.
            # (Implicitly, the batch size grows because 'i' moves forward)
            if current_val == next_val:
                continue
            
            # Batch Size:
            # Current index 'i' minus the start gives us how many items are in the current valley
            # e.g., if we are at index 0 and start is 0, batch is 1.
            batch_size = (i - consumer_start_index) + 1
            
            # GAP LOGIC:
            diff = next_val - current_val
            needed = diff * batch_size
            
            # "TEST OUT A METHOD" LOGIC (On Demand Fetching):
            # While we need energy and the stack pointer is valid, grab batteries!
            while current_spare_energy < needed and stack_ptr >= 0:
                current_spare_energy += batteries[stack_ptr]
                stack_ptr -= 1
            
            # Check if we have enough
            if current_spare_energy >= needed:
                # Pay the cost to jump to the next level
                current_spare_energy -= needed
                # We continue to the next loop, effectively merging with next_val
            else:
                # Not enough energy to make the full jump.
                # Use whatever is left to raise the current batch partially.
                return current_val + (current_spare_energy // batch_size)
        
        # 3. FINAL STEP:
        # If we exit the loop, we are at the level of the largest battery (batteries[-1]).
        # But we might still have untouched batteries in the stack!
        
        # Simply loop the remaining stack pointer
        while stack_ptr >= 0:
            current_spare_energy += batteries[stack_ptr]
            stack_ptr -= 1
            
        # Distribute remaining energy among ALL n computers
        return batteries[-1] + (current_spare_energy // n)