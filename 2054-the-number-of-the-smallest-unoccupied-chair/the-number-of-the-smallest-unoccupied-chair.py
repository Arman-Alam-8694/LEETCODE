class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        def binary_insert(numm):
            left=0
            right=len(available)-1
            while left<=right:
                mid=(left+right)//2
                if available[mid]>numm:
                    right=mid-1
                else:
                    left=mid+1
            return left

        arrival=[]
        leaving=[]
        target=times[targetFriend]
        for i,(a,l) in enumerate(times):
            arrival.append((a,i))
            leaving.append((l,i))
        arrival.sort()
        leaving.sort()
        occupied=[]
        dictt={}
        available=[i for i in range(len(times))]
        count=0
        a=0
        l=0
        n=len(arrival)+len(leaving)
        for i in range(n):
            min_leave=leaving[l][0]
            start=arrival[a][0]
    

            if start<min_leave:

                if start==target[0]:

                    return available[0]
                occupied.append(available[0])
                dictt[arrival[a][1]]=available[0]
                available.pop(0)
                a+=1
            else:
                f=leaving[l][1]
                chair=dictt[f]
                pos=binary_insert(chair)
                available.insert(pos,chair)
                l+=1
        return 0
            
            
        

        