import math
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def generate_primes(right,left):
            listt=[True]*(right+1)
            listt[0],listt[1]=False,False
            for i in range(2,right+1):
                if listt[i]==True:
                    for j in range(i*i,right+1,i):
                        listt[j]=False
        
            return [i for i in range(len(listt)) if i>=left and listt[i]==True]

        listt=generate_primes(right,left)
        
                
        minimum_dist=float('inf')
        result=[-1,-1]
        last_prime=None
      
        n=len(listt)

        for j in range(n-1):
         
            if listt[j+1]-listt[j]<minimum_dist:
                result[0]=listt[j]
                result[1]=listt[j+1]
                minimum_dist=listt[j+1]-listt[j]
                # if minimum_dist==2:
                #     return result

        return result




