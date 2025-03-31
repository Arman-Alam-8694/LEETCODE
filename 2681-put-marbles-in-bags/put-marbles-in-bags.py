class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        splits=[]
        n=len(weights)
        if k==1 or k==n:
            return 0
           
        for i in range(1,n):
            splits.append(weights[i]+weights[i-1])
        splits.sort()
        return sum(splits[-1*(k-1):])-sum(splits[:k-1])