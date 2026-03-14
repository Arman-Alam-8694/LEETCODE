class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        curr=[]
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
            
            
            for i in items:
                
                if i!=prev:
                    if len(curr)==n-1:
                        cnt+=1
                    curr.append(i)
                    stored,found=backtrack(curr)
                    if found:
                        return stored,True
                    curr.pop()
            return "",False

        ans,aa=backtrack([])
        res="".join(ans)
        return res
                

        