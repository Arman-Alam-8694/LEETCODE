class ProductOfNumbers:

    def __init__(self):
        self.product=[]
        self.numbers=[]
        self.last_zero=None
        self.idx=0
        

    def add(self, num: int) -> None:
    

        self.numbers.append(num)
        if num==0:
            self.last_zero=len(self.numbers)-1
        
            if self.product:
                self.product.append(self.product[-1])
            else:
                self.product.append(1)
        else:
            
        
            if self.product:
                self.product.append(self.product[-1]*num)
            else:
                self.product.append(num)

    def getProduct(self, k: int) -> int:

       
        if self.last_zero is not None:
            new_zero=len(self.numbers)-self.last_zero
            if k>=new_zero:
                return 0
        if k+1>len(self.product):
            return self.product[-1]
        else:
            return self.product[-1]//( self.product[-(k+1)]if self.product[-(k+1)]!=0 else 1)

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)