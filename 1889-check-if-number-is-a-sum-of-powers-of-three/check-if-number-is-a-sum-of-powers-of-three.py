class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            if n%3==2:
                return False
            n//=3
        return True
        
    #     return self.checkPowersOfThree(n-1)
    #     return self.helperpower(0,n)
    # def helperpower(self,power,n):
    #     if n==0:
    #         return True
    #     if n<3**power:
    #         return False
    #     addpower=self.helperpower(power+1,n-3**power)
    #     skippower=self.helperpower(power+1,n)
    #     return addpower|skippower

        
        