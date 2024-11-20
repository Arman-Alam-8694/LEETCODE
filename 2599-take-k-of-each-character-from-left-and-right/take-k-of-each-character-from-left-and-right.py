class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if len(s) < 3*k:
            return -1
        
        if k == 0:
            return 0
        
        d = Counter(s)

        if 'a' not in d or 'b' not in d or 'c' not in d:
            return -1
        
        if d['a'] < k or d['b'] < k or d['c'] < k:
            return -1

        def isPossible(size):
            d = Counter(s)

            for i in range(len(s)):
                d[s[i]] -= 1

                if i >= size:
                    d[s[i-size]] += 1
                
                if i >= size-1 and d['a'] >= k and d['b'] >= k and d['c'] >= k:
                    return True
            
            return False
        
        l = 0
        r = len(s) - 1
        temp = 0
        while l <= r:
            mid = (l+r)//2
            if isPossible(mid):
                # print(mid)
                temp = mid
                l = mid + 1
            else:
                r = mid-1
        
        return len(s) - temp
        


        