class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxx=0
        count={0:1}
        for i in nums:
            current={}
            for k,v in count.items():
                new=i|k
                maxx=max(maxx,new)
                if new in current:
                    current[new]+=v
                else:
                    current[new]=v
            for k,v in current.items():
                if k in count:
                    count[k]+=v
                else:
                    count[k]=v
        return count[maxx]
