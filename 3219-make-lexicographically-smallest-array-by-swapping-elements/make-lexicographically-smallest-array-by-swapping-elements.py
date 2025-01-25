class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Pair each number with its original index
        indexed_nums = sorted(enumerate(nums), key=lambda x: x[1])
        
        # Group numbers that can be swapped
        groups = []
        current_group = [indexed_nums[0]]
        
        for i in range(1, len(indexed_nums)):
            if indexed_nums[i][1] - indexed_nums[i-1][1] <= limit:
                current_group.append(indexed_nums[i])
            else:
                groups.append(current_group)
                current_group = [indexed_nums[i]]
        
        # Add the last group
        groups.append(current_group)
        
        # Reconstruct the result
        result = [0] * len(nums)
        for group in groups:
            # Sort indices and values separately
            indices = sorted(idx for idx, _ in group)
            values = sorted(val for _, val in group)
            
            # Assign values to original indices
            for i in range(len(group)):
                result[indices[i]] = values[i]
        
        return result