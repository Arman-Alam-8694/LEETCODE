class Solution:
    def minimumSteps(self, s: str) -> int:
        prev=-1
        cont=0
        swaps=0
        for right in s:
            if prev=="1" and right=="0":
                if cont:
            
                    swaps+=cont
                    continue
                swaps+=1
                prev="1"
            elif prev=="1" and right=="1":
                if cont:
                    cont+=1
                else:
                    cont+=2
            elif prev=="0" and right=="1":
                prev="1"
            else:
                prev=right
        return swaps

      

        