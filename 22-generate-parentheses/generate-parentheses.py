class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        string=""
        result=[]
        def recur(n,opencnt,string):
            if opencnt==0 and len(string)==2*n:
                result.append(string)
            if len(string)>2*n:
                return
            if not string:
                recur(n,opencnt+1,string+"(")
            elif string[-1]=="(":
                recur(n,opencnt+1,string+"(")
                recur(n,opencnt-1,string+")")
            else:
                if opencnt==0:
                    recur(n,opencnt+1,string+"(")    
                else:
                    recur(n,opencnt-1,string+")")   
                    recur(n,opencnt+1,string+"(")         

        recur(n,0,"")
        return result
        