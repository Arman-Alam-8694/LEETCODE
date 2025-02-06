class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        mapp={}
        total=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                mult=nums[i]*nums[j]
                if mult not in mapp:
                    mapp[mult]=1
                else:
                    mapp[mult]+=1
        print(mapp)
        for key,val in mapp.items():
            temp=(val*(val-1))*4
            total+=temp

        return total
                

        