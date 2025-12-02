import random
class RandomizedSet:
    

    def __init__(self):
        self.stack=[]
        self.mapp={}
        
        

    def insert(self, val: int) -> bool:
        if val in self.mapp:
            return False
        else:
            self.mapp[val]=len(self.stack)
            self.stack.append(val)
            return True
     

        

    def remove(self, val: int) -> bool:
        if val in self.mapp:
            idx=self.mapp[val]
            if idx!=len(self.stack)-1:
                del self.mapp[val]
                last_val=self.stack[-1]
                self.mapp[last_val]=idx
              
                self.stack[-1],self.stack[idx]=self.stack[idx],self.stack[-1]
                
                self.stack.pop()
            else:
                del self.mapp[val]
                self.stack.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        idx=random.randrange(len(self.stack))
        return self.stack[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()