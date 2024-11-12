class Solution:
    def countPrimes(self, n: int) -> int:
        # primes=[True]*(n)
        # count=0
        # if n==1 or n==0 :
        #     return 0
        
        # last=int(n**0.5)
        # for i in range(2,last+1):
        #     if primes[i]:
        #         count+=1
        #         for j in range(i*i,n,i):
        #             primes[j]=False
            
        # for i in range(last+1,n):
        #     if primes[i]:
        #         count+=1
        # return count
        if n<2:
            return 0
        primes=[True]*(n)
        primes[0]=False
        primes[1]=False
    
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i,n,i):
                    primes[j]=False
        
        return sum(primes)


        