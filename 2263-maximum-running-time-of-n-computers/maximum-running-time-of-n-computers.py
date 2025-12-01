class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        
        # 1. Separate into your logic's components
        # 'stack' is the spare energy pool
        # 'consumer' is the active computers (the n largest batteries)
        stack = batteries[:-n]
        consumer = batteries[-n:]
        
        # 2. Instead of a loop popping one by one, we sum the stack
        # This represents the total fluid "extra" power we can distribute.
        extra = sum(stack)
        
        # 3. "Heap" Logic simulation:
        # We iterate through the active batteries from smallest to largest.
        # This is mathematically identical to popping from a min-heap repeatedly.
        for i in range(n - 1):
            # current_height is the runtime of the i-th smallest computer
            current_height = consumer[i]
            # next_height is the runtime of the next smallest computer
            next_height = consumer[i + 1]
            
            # The gap we want to fill to make the current computer equal to the next one
            diff = next_height - current_height
            
            # CRITICAL LOGIC:
            # Since we have flattened everything up to index 'i', 
            # there are actually (i + 1) computers currently at 'current_height'.
            # To raise ALL of them to 'next_height', we need:
            needed = diff * (i + 1)
            
            if extra >= needed:
                # If we have enough extra juice, fill the gap and continue
                extra -= needed
            else:
                # If we DON'T have enough to reach the next level, 
                # we spread the remaining extra evenly among the (i + 1) computers
                return current_height + (extra // (i + 1))
        
        # 4. If we exit the loop, it means we flattened all n computers to the level 
        # of the largest battery, and we STILL have extra energy.
        # So we add the remaining extra evenly across all n computers.
        return consumer[-1] + (extra // n)