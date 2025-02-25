from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        odd_indices = [ i for i in range(n) if arr[i]&1]
        k = len(odd_indices)
        prev_even_sum=0
        prev_odd_sum=0
        result = 0

        for i in range(k):
            result+=1
            cur_idx=odd_indices[i]
            left=0
            right=0
            a,b=0,0
            if i>0:
                left=odd_indices[i-1]
                a=(cur_idx-left)-1
            else:
                if cur_idx!=0:
                    left=0
                    a=(cur_idx-left)
            if i<k-1:
                right=odd_indices[i+1]
                b=(right-cur_idx)-1
            else:
                if cur_idx!=n-1:
                    right=n-1
                    b=(right-cur_idx)
            result+=(a+b)
            result+=(a*b)

            if i%2==0:
                result+=prev_even_sum
                result+=(prev_even_sum*b)
                prev_even_sum+=(1+a)
      
            else:
                result+=prev_odd_sum
                result+=(prev_odd_sum*b)
                prev_odd_sum+=(1+a)
        return result%MOD


