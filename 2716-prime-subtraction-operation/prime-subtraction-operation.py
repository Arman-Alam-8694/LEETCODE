class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Brute force prime generation O(n²)
        def generatePrimes(n):
            primes = []
            for num in range(2, n + 1):
                is_prime = True
                # Check if num is divisible by any number up to num
                for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)
            return primes

        primes = generatePrimes(1000)
        
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
                if find <= 0:
                    return False
                sub = binsearch(find, primes)
                if sub >= nums[i] or sub == -1:
                    return False
                nums[i] = nums[i] - sub
        
        return True