class Solution:
    def makeFancyString(self, s: str) -> str:
        count=0
        chr=""
        result=[]
        i=0
        while i<len(s):
            if chr!=s[i]:
                count=0
                chr=s[i]
                continue
            count+=1
            if count==3:
                count-=1
                i+=1
                continue
            result.append(chr)
            i+=1
        return "".join(result)
        