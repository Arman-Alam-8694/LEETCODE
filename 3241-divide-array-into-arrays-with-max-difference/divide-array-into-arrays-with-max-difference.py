class Solution:
    def divideArray(self, num: List[int], k: int) -> List[List[int]]:
        # nums.sort()
        #using sort gives nlogn we will use counting sort and rebuild the sorted array
        store=[0]*(max(num)+1)
        for i in num:
            store[i]+=1

        nums=[]
        for i in range(len(store)):
            nums.extend([i]*store[i])
        

        result=[[]]
        temp=[]
        for i in nums:
            result[-1].append(i)
            if result[-1] and result[-1][-1]-result[-1][0]>k:
                return []
            if len(result[-1])==3:
                result.append([])
        result.pop()
        return result