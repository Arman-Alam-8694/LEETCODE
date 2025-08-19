class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result=0
        left=0
        mapp=defaultdict(int)
        for right in range(len(nums)):
            mapp[nums[right]]+=1
            while len(mapp)>1 :
                mapp[nums[left]]-=1
                if mapp[nums[left]]==0:
                    del mapp[nums[left]]
                left+=1
            if len(mapp)==1 and (0 in mapp.keys()):
                result+=(right-left+1)
        return result
            

        