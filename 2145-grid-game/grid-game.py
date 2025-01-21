from collections import deque
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        #time complexity O(n) space complexity O(n)
        # row=2
        # col=len(grid[0])
        # prefix_first=[0]*col
        # prefix_second=[0]*col
        # prefix_a,prefix_b=0,0
        # for i in range(col):
        #     prefix_a+=grid[0][i]
        #     prefix_b+=grid[1][i]
        #     prefix_first[i]=prefix_a
        #     prefix_second[i]=prefix_b

     
        # result=float('inf')
        # for i in range(col):
        #     right=prefix_first[-1]-prefix_first[i]
        #     left=prefix_second[i-1] if i!=0 else 0
        #     temp=max(right,left)
        #     result=min(temp,result)
     

        # return result

        #constant space and time O(1)
        col = len(grid[0])
        
        # Compute the total sums of both rows
        total_top = sum(grid[0])
        total_bottom = 0
        
        result = float('inf')
        
        for i in range(col):
            # Points remaining on the top row after column i
            right = total_top - grid[0][i]
            
            # Points collected on the bottom row up to column i
            left = total_bottom
            
            # Maximum points the second robot can collect
            temp = max(right, left)
            result = min(result, temp)
            
            # Update the cumulative sums
            total_top -= grid[0][i]
            total_bottom += grid[1][i]
        
        return result
        
        









        