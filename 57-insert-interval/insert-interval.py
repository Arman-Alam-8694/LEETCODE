class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        result=[]
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if intervals[mid][0]>=newInterval[0]:
                right=mid-1
            else:
                left=mid+1
        # print(left,right)
        intervals.insert(left,newInterval)
        n=len(intervals)
        for i in range(0,left):
            result.append(intervals[i])
        # print(result,intervals)
        start=left
        if not result:
            result=[intervals[0]]
            start=1
        for i in range(start,n):
            if result[-1][0]!=intervals[i][0] and result[-1][1]<intervals[i][0]:
                # print("here")
                result.append(intervals[i])
            else:
                srt,end=result.pop()
                nsrt=min(srt,intervals[i][0])
                nend=max(end,intervals[i][1])
                result.append([nsrt,nend])
        return result