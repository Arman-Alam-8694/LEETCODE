class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        candidates=['a','b','c']
        cnt=0
        def backtrack(stringg):
            nonlocal cnt
            if len(stringg)==n:
                cnt+=1
                return stringg
            for i in candidates:
                if not stringg or stringg[-1]!=i:
                    stringg.append(i)
                    return_val=backtrack(stringg)
                    if cnt==k:
                        return return_val
                    stringg.pop()
                    
        result=backtrack([])
        if result:
            return "".join(result)
        return ""
    

            