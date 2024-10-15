class Solution:
    def minimumSteps(self, s: str) -> int:
        cont=0
        swaps=0
        for right in s:
            if right=="1":
                cont+=1
            else:
                swaps+=cont
        return swaps

      

        