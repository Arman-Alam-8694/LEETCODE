class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        #using sort gives nlogn we will use counting sort and rebuild the sorted array
        # store=[0]*(max(num)+1)
        # for i in num:
        #     store[i]+=1

        # nums=[]
        # for i in range(len(store)):
            # nums.extend([i]*store[i])
        #i tried using the counting sort but i think the test cases are not good enought
        #for this approach because if the array consist of number like 
        #1 2 3 398393893
        #so the max of this array is very huge so if we use the couting sort then 
        #we have to first make the array of that size and then cound and rebuild 
        #so at the tnd nlogn for this type of test cases are much better
        #so i think that's why the overall runtime of this solution using the count sort 
        #is comparatively slower than the nlogn simple sort solution
        

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