class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        string=""
        result=[]
       
        def recur(opencnt,closecnt,string):
            if len(string)==2*n:
                result.append(string)
                return 
            if opencnt<n:
                recur(opencnt+1,closecnt,string+"(")    
            if opencnt>closecnt:
                recur(opencnt,closecnt+1,string+")")        

        recur(0,0,"")
        return result
        