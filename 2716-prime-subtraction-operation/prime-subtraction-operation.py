class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes=[]
        for i in range(2,1000):
         
            isPrime=True
            for k in range(2,int(i**0.5)+1):
                if i%k==0:
                    isPrime=False
                    break
            if isPrime:
                primes.append(i)
        # print(primes)
        def binsearch(find,primes):
            length=len(primes)
            left=0
            right=length-1
            while left<=right:
                mid=(left+right)//2
                if primes[mid]>find:
                    right=mid-1
                elif primes[mid]==find:
                    return primes[mid]
                else:
                    left=mid+1
            if len(primes)>left>=0:
                return primes[left]
            return -1
        
        for i in range(len(nums)-2,-1,-1):
            
            if nums[i]>=nums[i+1]:
             
                find=(nums[i]-nums[i+1])+1
                if find<=0:
                    return False
                sub=binsearch(find,primes)
                print(find,sub,nums[i])
                if sub>=nums[i] or sub==-1:
                    return False
                nums[i]=nums[i]-sub
                print(nums)
               


            
        return True

