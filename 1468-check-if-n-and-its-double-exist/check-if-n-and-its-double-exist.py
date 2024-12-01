class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mapp={}
        n=len(arr)
        for i in range(n):
            mapp[arr[i]]=i
        for i in range(n):
            number=arr[i]*2
            if number in mapp:
                if i!=mapp[number]:
                    return True
        return False


        