class Solution:
    def compressedString(self, word: str) -> str:
        result=[]
        dictt={}
        for i in word:
            if i not in dictt:
                if len(dictt)==1:
                    chr,count=list(dictt.items())[0]
                    result.append(str(count))
                    result.append(chr)
                    dictt.clear()
                dictt[i]=1
            else:
                dictt[i]+=1
                if dictt[i]==9:
                    chr,count=list(dictt.items())[0]
                    result.append(str(count))
                    result.append(chr)
                    dictt.clear()
                    continue
        if dictt:
            chr,count=list(dictt.items())[0]
            result.append(str(count))
            result.append(chr)
        return "".join(result)
            
            
        