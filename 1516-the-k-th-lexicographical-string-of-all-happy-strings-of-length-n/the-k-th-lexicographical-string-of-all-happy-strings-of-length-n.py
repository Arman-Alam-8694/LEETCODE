class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        curr=""
        items=['a','b','c']
        cnt=0
        def backtrack(curr):
            nonlocal cnt       
            if len(curr)==n and cnt==k:
                return  curr,True
            if len(curr)>n:
                return "",False
            if curr:
                prev=curr[-1]
            else:
                prev=""
            
            print(curr,cnt)
            for i in items:
                
                if i!=prev:
                    if len(curr)==n-1:
                        cnt+=1
                    stored,found=backtrack(curr+i)
                    if found:
                        return stored,True
            return "",False

        ans,aa=backtrack(curr)
        return ans
                

        