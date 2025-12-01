import heapq

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        
        # 1. Separate Stack (extra juice) and Consumers (active computers)
        stack_sum = sum(batteries[:-n])
        consumer = batteries[-n:]
        
        # 2. Turn consumers into a Min-Heap
        heapq.heapify(consumer)
        
        # 3. Initialize the 'batch'
        # We pop the first smallest battery to start
        current_min = heapq.heappop(consumer)
        batch_size = 1
        
        # 4. Loop while we still have other distinct batteries to catch up to
        while consumer:
            # PEEK: Check the next smallest battery in the heap
            next_min = consumer[0]
            
            # DISTINCT LOGIC:
            # If the next battery in the heap is equal to what we currently have,
            # we don't need to fill any gap. We just add it to our "batch"
            # and pop it out of the heap.
            if next_min == current_min:
                heapq.heappop(consumer)
                batch_size += 1
                continue
            
            # CALCULATE GAP:
            # We need to raise all 'batch_size' computers from 'current_min' to 'next_min'
            diff = next_min - current_min
            needed = diff * batch_size
            
            if stack_sum >= needed:
                # We have enough extra juice!
                stack_sum -= needed
                # Effectively, all computers in our batch are now at 'next_min'
                current_min = next_min 
            else:
                # We don't have enough juice to reach the next distinct level.
                # Spread remaining juice evenly among the current batch and stop.
                return current_min + (stack_sum // batch_size)
        
        # 5. If the heap is empty, it means we flattened ALL n computers 
        # to the level of the largest battery. 
        # Divide remaining stack_sum among all n computers.
        return current_min + (stack_sum // n)