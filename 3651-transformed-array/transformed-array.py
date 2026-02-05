class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        for i in range(n):
            val=nums[i]
 
            if val>0:
                nxt=(i+val)%n
                result[i]=nums[nxt]

            elif val<0:
                nxt=(((n-1)-i)-val)%n
                # nxt=(n+i+val)%n
                result[i]=nums[(n-1)-nxt]
            else:
                result[i]=0
        return result
            

    # 0 1 2 3 4 5

        