from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        # odd_indices = [ i for i in range(n) if arr[i]&1]
        # k = len(odd_indices)
        # prev_even_sum=0
        # prev_odd_sum=0
        # result = 0
        #IN THIS ONE THE IDEA IS TO USE THE INDEXES OF THE ODD NUMBER TO FIND THE SUBARRAY WE FIRST AT EACH ODD INDEX CALCULATE THE POSSIBLE SUBARRAY INLCUDING 
        #JUST THAT ELEMENT AND THEN WE TRY TO FORM THE ODD NUMBER OF PAIRS OF ODD NUMBERS BECAUSE ODD NUMBER OF ODD'S NUMBER WILL ONLY YEILD US ODD SUM FOR 
        #EXAMPLE 1 ,1+3 NOT GIVES US ODD, 1+3+5 GIVES US ODD ,1+3+5+7+9 AGAIN ODD
        #THIS SOLUTION IS SLOW ALSO TAKES THE MORE AMOUNT OF SPACE COMPARED TO THE BELOW SOLUTION 

        # for i in range(k):
        #     result+=1
        #     cur_idx=odd_indices[i]
        #     left=0
        #     right=0
        #     a,b=0,0
        #     if i>0:
        #         left=odd_indices[i-1]
        #         a=(cur_idx-left)-1
        #     else:
        #         if cur_idx!=0:
        #             left=0
        #             a=(cur_idx-left)
        #     if i<k-1:
        #         right=odd_indices[i+1]
        #         b=(right-cur_idx)-1
        #     else:
        #         if cur_idx!=n-1:
        #             right=n-1
        #             b=(right-cur_idx)
        #     result+=(a+b)
        #     result+=(a*b)

        #     if i%2==0:
        #         result+=prev_even_sum
        #         result+=(prev_even_sum*b)
        #         prev_even_sum+=(1+a)
      
        #     else:
        #         result+=prev_odd_sum
        #         result+=(prev_odd_sum*b)
        #         prev_odd_sum+=(1+a)
        # return result%MOD


        #prefix subarray sum using the counts of even and odds sum of the array to determine the odd coutn
        #for example we have even runsum then we have to remove the oddCnts to get the odd sum of the   array
        #3+3=6 we can remove the 3 subarray with odd sum to get the odd sum again 
        #4+2=6 we cant' form any odd sum subarray because there is no odd sub array to be removed
        #similarly for the odd runsum we have to remove the evenCnts to get the odd sum of the array
        #3+4=7 we have to remove the 4 to get the odd
        oddCnts=0
        evenCnts=0
        runsum=0
        result=0
        for i in arr:
            runsum+=i
            if runsum&1:
                oddCnts+=1
                result+=1
                result+=evenCnts
            else:
                evenCnts+=1
                result+=oddCnts
        return result%MOD



