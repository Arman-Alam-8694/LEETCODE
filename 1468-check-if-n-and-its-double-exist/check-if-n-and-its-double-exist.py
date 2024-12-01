class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mapp={}
        n=len(arr)
        for i in range(n):
            if (arr[i])/2 in mapp or (arr[i])*2 in mapp:
                return True
            mapp[arr[i]]=i
        return False

        