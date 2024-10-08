class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors=[]
        for i in range(1,int((n**0.5))+1):
            if n%i==0:
                if n//i!=i:
                    factors.append(n//i)
                factors.append(i)
        factors.sort()
        if k>len(factors):
            return -1
        else:
            return factors[k-1]
        