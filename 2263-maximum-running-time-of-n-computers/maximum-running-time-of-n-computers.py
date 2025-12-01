class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # 1. Sort to separate 'stack' and 'consumer'
        batteries.sort()
        
        # 'stack' (rest of the elements): We take their total energy
        extra_power = sum(batteries[:-n])
        
        # 'consumer' (largest n elements): These are our active computers
        # This sorted list acts as your "Min Heap" + "Distinct Array" combined.
        # consumer[i] is the current smallest, consumer[i+1] is the next target.
        consumer = batteries[-n:]
        
        # We iterate through the consumers to "level them up"
        for i in range(n - 1):
            # The current smallest battery (simulating the 'pop')
            current_val = consumer[i]
            
            # The next distinct target (simulating the 'peek')
            next_val = consumer[i + 1]
            
            # If they are already equal, we just expand our batch size (continue loop)
            if current_val == next_val:
                continue
            
            # YOUR LOGIC: "suppose it becomes equal to 2 3 elements"
            # Since we are at index 'i', it means indices 0 to i (total i+1 computers)
            # are all currently flattened at 'current_val'.
            computers_in_batch = i + 1
            
            # Calculate power needed to raise ALL these computers to the next level
            diff = next_val - current_val
            needed = diff * computers_in_batch
            
            if extra_power >= needed:
                # We have enough juice to raise this whole batch to the next level
                extra_power -= needed
                # Conceptually, consumer[0...i] are now all equal to consumer[i+1]
            else:
                # We don't have enough juice to reach the next level.
                # Use the remaining extra_power to raise the batch as high as possible.
                return current_val + (extra_power // computers_in_batch)
        
        # If the loop finishes, all n computers have been raised to the level of the
        # largest original battery. We distribute any remaining extra power evenly.
        return consumer[-1] + (extra_power // n)