from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        available = Counter(tiles)  
        count = 0  

        def backtrack():
            nonlocal count
            for tile in available:
                if available[tile] > 0:
                    available[tile] -= 1  
                    count += 1  
                    
                    backtrack() 
                    
                    available[tile] += 1  
        
        backtrack()
        return count


