class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Sieve of Eratosthenes for generating primes up to 1000
        n=1000
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                # Mark all multiples as non-prime
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        
        primes=[i for i in range(2, n + 1) if sieve[i]]

    
       
        
        def binsearch(find, primes):
            length = len(primes)
            left = 0
            right = length - 1
            while left <= right:
                mid = (left + right) // 2
                if primes[mid] > find:
                    right = mid - 1
                elif primes[mid] == find:
                    return primes[mid]
                else:
                    left = mid + 1
            if len(primes) > left >= 0:
                return primes[left]
            return -1
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                find = (nums[i] - nums[i + 1]) + 1
                if find>997 or find<=0:
                    return False
               
                sub = binsearch(find, primes)
                if sub >= nums[i] or sub == -1:
                    return False
                nums[i] = nums[i] - sub
        
        return True