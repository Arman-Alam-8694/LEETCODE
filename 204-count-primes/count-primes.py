class Solution:
    def countPrimes(self, n: int) -> int:
        primes=[True]*(n)
        count=0
        if n==1 or n==0 or n==2:
            return 0
        
        last=int(n**0.5)+1
        for i in range(2,last+1):
            if primes[i]:
                count+=1
                for j in range(i*i,n,i):
                    primes[j]=False
            
        for i in range(last+1,n):
            if primes[i]:
                count+=1
        return count

        