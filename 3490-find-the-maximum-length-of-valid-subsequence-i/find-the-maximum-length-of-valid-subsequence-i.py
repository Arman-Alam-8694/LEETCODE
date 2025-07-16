class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        result=0
        for case in [(0,0),(1,1),(0,1),(1,0)]:
            prev=None
            idx=0
            cur=case[0]
            temp=0
            for i in nums:
                if i%2==cur:
                    idx=1 if idx==0 else 0
                    cur=case[idx]
                    temp+=1

            result=max(result,temp)
        return result


        