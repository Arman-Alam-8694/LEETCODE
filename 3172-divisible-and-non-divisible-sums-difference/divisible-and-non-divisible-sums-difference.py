class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # div=0
        # notdiv=0
        # for i in range(1,n+1):
        #     if i%m==0:
        #         div+=i
        #     else:
        #         notdiv+=i
        # return notdiv-div
        
        #BETTER SOLUTION O(1) TC

        #no of multiples upto n of m
        k=n//m
        #sum of these 
        # num2=(k*(k+1)//2)*m
        #we know num1+num2=total
        #so num1=total-num2 and we already have num2 and by substituing we get
        #n*(n+1)//2-k*(k+1)*m
        return n*(n+1)//2-k*(k+1)*m
