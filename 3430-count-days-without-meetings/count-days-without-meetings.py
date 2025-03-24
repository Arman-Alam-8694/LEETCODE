class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # meetings.sort(key=lambda x:x[0])
        # maxx=0
        # for s,e in meetings:
        #     maxx=max(maxx,max(s,e))
        # temp=[0]*(maxx+1)
        # for s,e in meetings:
        #     temp[e]-=1
        #     temp[s-1]+=1
        # result=0
        # rem=days-maxx
        # run=0
        # for d in temp:
        #     run+=d
        #     if run==0:
        #         result+=1
        # return result+rem-1

        left=float("inf")
        right=-1
        meetings.sort(key=lambda x:x[0])
        timing=[]
        for s,e in meetings:
            if s>right:
                timing.append((left,right))
                left=s
                right=e
            else:
                if e>right:
                    right=e
        run=0
        timing.append((left,right))
        print(timing)
        for t in range(1,len(timing)):
            run+=(timing[t][1]-timing[t][0])+1
        return days-run
            


