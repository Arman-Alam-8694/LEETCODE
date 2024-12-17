class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod=(10**9)+7
        oddsum,evensum,res,runsum=0,0,0,0
        for n in arr:
            runsum+=n
            if runsum&1:
                oddsum+=1
                res+=evensum+1
            else:
                evensum+=1
                res+=oddsum
        return res%mod
        