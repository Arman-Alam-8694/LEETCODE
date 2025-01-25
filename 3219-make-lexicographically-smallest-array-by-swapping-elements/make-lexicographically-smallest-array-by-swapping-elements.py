class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups=[]
        elementtogroup={}
        num=sorted(nums)
        result=[]
        n=len(nums)
        temp=deque()
        last=num[0]
        idx=0
        for i in range(n):
            if abs(num[i]-last)<=limit:
                temp.append(num[i])
                elementtogroup[num[i]]=idx
                last=num[i]
            else:
                groups.append(temp)
                idx+=1
                temp=deque()
                temp.append(num[i])
                last=num[i]
                elementtogroup[num[i]]=idx
        if temp:
            groups.append(temp)
        for i in nums:
            groupidx=elementtogroup[i]
            result.append(groups[groupidx].popleft())
        
       
        return result



            



        