class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result=[]
        if not digits:
            return result
        string="abcdefghijklmnopqrstuvwxyz"
        mapp={}
        start=0
        for i in range(2,10):
            if i==9 or i==7:
                mapp[str(i)]=string[start:start+4]
                start+=4
            else:
                mapp[str(i)]=string[start:start+3]
                start+=3
        def backtrack(idx,string):
            if len(string)==len(digits):
                result.append(string)
                return 
            for i in mapp[digits[idx]]:
                backtrack(idx+1,string+i)

        backtrack(0,"")
      
        return result
        