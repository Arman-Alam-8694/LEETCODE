class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban=set(banned)
        summ=0
        count=0
        for i in range(1,n+1):
            if i not in ban:
                summ+=i
                count+=1
            if summ>maxSum:
                return count-1
        return count
            

        