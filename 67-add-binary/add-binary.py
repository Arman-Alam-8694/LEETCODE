class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry="0"
        top=-1
        bottom=-1
        answer=[]
        while (-1*top)<=len(a) or (-1*bottom)<=len(b):
            t=a[top] if (-1*top)<=len(a) else "0"
            bb=b[bottom] if (-1*bottom)<=len(b) else "0"
            if t=="0":
                if bb=="0":
                    if carry=="1":
                        carry="0"
                        answer.append("1")
                    else:
                    
                        answer.append('0')
                else:
                    if carry=="1":
                        carry="1"
                        answer.append("0")
                    else:
                        answer.append("1")
            else:
                if bb=="0":
                    if carry=="1":
                        carry="1"
                        answer.append("0")
                    else:
                        carry="0"
                        answer.append('1')
                else:
                    if carry=="1":
                        carry="1"
                        answer.append("1")
                    else:
                        answer.append("0")
                        carry="1"
            top-=1
            bottom-=1
        if carry=="1":
            answer.append('1')

        answer=answer[::-1]
        return "".join(answer)
    

        