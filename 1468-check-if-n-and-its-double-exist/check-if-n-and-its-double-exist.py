class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mapp={}
        n=len(arr)
        for i in range(n):
            number=(arr[i])/2
            number1=(arr[i])*2
            if number in mapp:
                return True
            elif number1 in mapp:
                return True
            mapp[arr[i]]=i
        return False

        