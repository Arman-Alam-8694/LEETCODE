class Solution:
    def makeFancyString(self, s: str) -> str:
        count=1
        chr=None
        result=[]
        i=0
        prev=None
        for i in s:
            if prev==i:
                count+=1
            else:
                count=1
            prev=i
            if count<3:
                result.append(prev)
        return "".join(result)
        