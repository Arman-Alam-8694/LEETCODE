class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def helper(pat1,pat2,xx,yy):
            score=0
            stack=[]
            for i in s:
                if stack and stack[-1]+i==pat1:
                    stack.pop()
                    score+=xx
                else:
                    stack.append(i)
            second=[]
            for i in stack:
                if second and second[-1]+i==pat2:
                    second.pop()
                    score+=yy
                else:
                    second.append(i)
            return score
        
        if x>=y:
            xx=x
            pat1="ab"
            pat2="ba"
            yy=y
        else:
            xx=y
            yy=x
            pat2="ab"
            pat1="ba"
        
        return helper(pat1,pat2,xx,yy)

            

