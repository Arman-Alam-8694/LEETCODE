class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result=1
        left=0
        for right in range(1,len(prices)):
            result+=1
            if prices[right-1]==prices[right]+1:
                result+=(right-left)        
            else:
                left=right
        return result