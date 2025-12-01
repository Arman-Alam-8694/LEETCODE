import heapq

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        
        # 1. The Stack is a list of batteries (we do NOT sum them yet)
        stack = batteries[:-n]
        
        # 2. The Consumers: largest N batteries in a heap
        consumer = batteries[-n:]
        heapq.heapify(consumer)
        
        # We hold 'loose' energy here that we've taken from the stack but haven't used yet
        current_spare_energy = 0
        
        # Initial State
        current_min = heapq.heappop(consumer)
        batch_size = 1
        
        while consumer:
            next_min = consumer[0]
            
            # DISTINCT LOGIC: 
            # If the next computer is same height, just add to batch and continue
            if next_min == current_min:
                heapq.heappop(consumer)
                batch_size += 1
                continue
            
            # GAP LOGIC:
            # We found a gap. We need this much energy to level up the whole batch.
            diff = next_min - current_min
            needed = diff * batch_size
            
            # "TEST OUT A METHOD" LOGIC:
            # We don't have a total sum. We have a 'stack' list.
            # While we don't have enough energy in our hand, go fetch more batteries from stack.
            while current_spare_energy < needed and stack:
                current_spare_energy += stack.pop() # Take one battery from the pile
            
            # NOW check if we have enough
            if current_spare_energy >= needed:
                # We have enough! Pay the cost.
                current_spare_energy -= needed
                # Level up!
                current_min = next_min
                # Important: We essentially merged with the next_min, so we add it to batch
                heapq.heappop(consumer)
                batch_size += 1
            else:
                # Stack is empty and we still don't have enough energy.
                # Use whatever we have left in 'current_spare_energy'
                return current_min + (current_spare_energy // batch_size)

        # FINAL STEP:
        # If heap is empty, we flattened all N computers to the top level.
        # We might still have batteries left in the stack list!
        
        # 1. Add remaining loose energy
        while stack:
            current_spare_energy += stack.pop()
            
        # 2. Distribute it evenly
        return current_min + (current_spare_energy // n)