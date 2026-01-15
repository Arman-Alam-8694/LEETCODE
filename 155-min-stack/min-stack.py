class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack and self.minstack[-1]>=val:
            self.minstack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        
        

    def pop(self) -> None:
        temp=self.stack.pop()
        if self.minstack and self.minstack[-1]==temp:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your self.minstack object will be instantiated and called as such:
# obj = self.minstack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()