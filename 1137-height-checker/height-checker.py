class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Calculate the maximum element in the list
        max_height = max(heights)
        
        # Create a counting array for frequencies
        count = [0] * (max_height + 1)
        
        # Count the occurrences of each height
        for height in heights:
            count[height] += 1
        
        # Simulate the sorted order and count mismatches directly
        index = 0
        mismatches = 0
        
        for height in range(1, max_height + 1):
            while count[height] > 0:
                if heights[index] != height:
                    mismatches += 1
                index += 1
                count[height] -= 1
        
        return mismatches
