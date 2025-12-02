import random 
class RandomizedCollection:

    def __init__(self):
        self.stack=[]
        self.mapp={}
        

    def insert(self, val: int) -> bool:
        new_idx=len(self.stack)
        self.stack.append(val)
        if val in self.mapp:
            ans=False
            self.mapp[val].add(new_idx)
        else:
            self.mapp[val]=set()
            self.mapp[val].add(new_idx)
            ans=True
        return ans
        

    def remove(self, val: int) -> bool:
        if val not in self.mapp:
            return False
        del_idx=self.mapp[val].pop()
        last_idx=len(self.stack)-1
        last_val=self.stack[-1]
        if del_idx!=last_idx:
            self.mapp[last_val].remove(last_idx)
            self.mapp[last_val].add(del_idx)
            self.stack[del_idx],self.stack[last_idx]=self.stack[last_idx],self.stack[del_idx]
            self.stack.pop()

        else:

            self.stack.pop()
        if not self.mapp[val]:
            del self.mapp[val]
        return True


        

    def getRandom(self) -> int:
        return self.stack[random.randrange(len(self.stack))]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()