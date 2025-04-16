class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        mapp={}
        left=0
        n=len(nums)
        result=0
        run=0
        for right in range(n):
            if nums[right] not in mapp:
                mapp[nums[right]]=1
            else:
                run+=mapp[nums[right]]
                mapp[nums[right]]+=1
            # if k==run:
            #     result+=1
            #     continue
            # print(run)
        
            while run>=k:
                result+=(n-right)
                # print(mapp)
                if mapp[nums[left]]>1:
                    run-=(mapp[nums[left]]-1)
                    mapp[nums[left]]-=1
                else:
                    del mapp[nums[left]]
                left+=1
                
        return result





        