class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        free_space=[]
        prev_start=0
        for i in range(len(startTime)):
            free_space.append(startTime[i]-prev_start)
            prev_start=endTime[i]
        if prev_start<eventTime:
            free_space.append(eventTime-prev_start)
        # print(free_space)
        prefix_sum=[0]*len(free_space)
        prefix_sum[0]=free_space[0]
        for i in range(1,len(free_space)):
            prefix_sum[i]=free_space[i]+prefix_sum[i-1]
        # print(prefix_sum)

        result=0
        if len(free_space)<=k:
            return prefix_sum[-1]
        for i in range(0,len(free_space)-k):
            # print(i)
            new=prefix_sum[i+k]-(prefix_sum[i-1] if i!=0 else 0)
            result=max(result,new)
        
        return result
        