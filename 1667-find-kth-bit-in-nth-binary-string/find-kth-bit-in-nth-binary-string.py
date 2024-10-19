class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(part):
            length=len(part)
            num=int(part,2)
            mask=int("1"*length,2)
            res=num^mask

            ans=bin(res)[2:]
            return ans

        stringg=""
        for i in range(n):
            if not stringg:
                stringg+="0"
                print(i,stringg)
                continue
            stringg=stringg+"1"+invert(stringg)[::-1]
        
  
        return stringg[k-1]
            

        