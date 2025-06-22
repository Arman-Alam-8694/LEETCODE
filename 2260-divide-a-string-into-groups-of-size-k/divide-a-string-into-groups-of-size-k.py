class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result=[]
        for i in range(0,len(s),k):
            temp=s[i:i+k]
            ln=len(temp)
            if ln!=k:
                temp+=fill*(k-ln)
            result.append(temp)

        return result


        