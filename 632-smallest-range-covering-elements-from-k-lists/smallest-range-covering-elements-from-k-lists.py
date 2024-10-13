class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_val = float('-inf')
        
        # Initialize the heap with the first element from each list
        for i, num_list in enumerate(nums):
            if num_list:
                heapq.heappush(min_heap, (num_list[0], i, 0))
                max_val = max(max_val, num_list[0])
        
        result = [float('-inf'), float('inf')]
        
        while len(min_heap) == len(nums):
            min_val, list_index, element_index = heapq.heappop(min_heap)
            
            # Update the result if we find a smaller range
            if max_val - min_val < result[1] - result[0] or (max_val - min_val == result[1] - result[0] and min_val < result[0]):
                result = [min_val, max_val]
            
            # Move to the next element in the list
            if element_index + 1 < len(nums[list_index]):
                next_val = nums[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_val, list_index, element_index + 1))
                max_val = max(max_val, next_val)
        
        return result
            