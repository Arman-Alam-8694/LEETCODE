class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # find all primes <= sqrt(right)
        primes = [2, 3]
        # only need to check up to ceil(sqrt(right))
        mx = int(right ** 0.5) + 1
        for k in range(5, mx, 2):
            isPrime = True
            for p in primes:
                if k % p == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(k)
        #print(f"primes={primes}")
        
        primesSet = set(primes)
        k = left
        if k % 2 == 0:
            k += 1
        lastPrime = -1
        minDiff = -1
        r = [-1, -1]
        while k <= right:
            if k == 1:
                lastPrime = 2
                k += 2
                continue
            isPrime = True
            if k not in primesSet:
                for p in primes:
                    if k % p == 0:
                        isPrime = False
                        break
            #print(f"k={k} isPrime={isPrime} lastPrime={lastPrime} minDiff={minDiff} r={r}")
            if isPrime:
                if lastPrime != -1 and (minDiff == -1 or k - lastPrime < minDiff):
                    r = [lastPrime, k]
                    minDiff = k - lastPrime
                lastPrime = k
            # no need to check further
            if minDiff == 2:
                break
            k += 2
        return r
        
        