class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res=0
        left=0
        summ=0
        cnt=0
        for right in range(len(nums)):
            summ+=nums[right]
            cnt+=1
            temp=summ*cnt
            # print(temp)
            if temp<k:
                res+=(right+1)-left
            else:
                while summ*cnt>=k and left<=right:
                    summ-=nums[left]
                    cnt-=1
                    left+=1
                # print("exceeded",left,right,cnt,summ)
                res+=(right+1)-left 
        
            

        return res


        