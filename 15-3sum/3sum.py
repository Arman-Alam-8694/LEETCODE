class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        sett=set(i for i in arr)
        if len(sett)==1:
            for i in sett:
                if i==0:
                    return [[0,0,0]]

        n=len(arr)
        answer=set()
        dictt={arr[0]:[0]}
        for i in range(1,n):
            for j in range(i+1,n):
                comp=-1*(arr[i]+arr[j])
           
                if comp in dictt:
                    temp=(comp,arr[i],arr[j])
                    answer.add(tuple(sorted(temp)))
            if arr[i] not in dictt:
                dictt[arr[i]]=1

        answer=list(answer)
       
     
        return answer
                        
                    