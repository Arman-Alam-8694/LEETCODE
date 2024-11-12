from bisect import bisect_right
from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        mapp = {}
        maxx = float('-inf')
        
        for i, j in items:
            maxx = max(maxx, j)
            mapp[i] = maxx  # Update the maximum beauty for each price
        
        # Extract sorted prices and their maximum beauty values for binary search
        prices = list(mapp.keys())
        beauties = list(mapp.values())
        
        result = []
        for query in queries:
            idx = bisect_right(prices, query) - 1  # Get the rightmost price <= query
            
            if idx >= 0:
                result.append(beauties[idx])  # Append the maximum beauty at that price
            else:
                result.append(0)  # No valid items for query price
                
        return result
