class Solution:
    def compressedString(self, word: str) -> str:
        result=[]
        curr=""
        count=0
        for i in word:
            if not curr:
                curr=i
                count=1
            elif curr!=i:
                result.append(str(count))
                result.append(curr)
                curr=i
                count=1 
            else:
                count+=1
                if count==9:
                    result.append(str(count))
                    result.append(curr)
                    curr=""
                    count=0 
        if curr:
            result.append(str(count))
            result.append(curr)

            
        return "".join(result)
            
            
        