class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res=0
        cur_max=values[0]-1
        for i in range(1,len(values)):
            res=max(res,cur_max+values[i])
            cur_max=max(values[i]-1,cur_max-1)
        return res
        