class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        result=[]
        n=len(code)
        b=["electronics","grocery","pharmacy","restaurant"]
        e=[]
        g=[]
        p=[]
        r=[]
        def check(stringg):
            if not stringg:
                return False
            for i in stringg:
                if i.isalnum() or i=="_":
                    continue
                else:
                    return False
            return True

        for i in range(n):
            if isActive[i] and (businessLine[i] in b) and check(code[i]):
                if businessLine[i]=="electronics":
                    e.append(code[i])
                elif businessLine[i]=="grocery":
                    g.append(code[i])
                elif businessLine[i]=="pharmacy":
                    p.append(code[i])
                else:
                    r.append(code[i])

        e.sort()
        g.sort()
        p.sort()
        r.sort()
        print(e,g,p,r)
        return e+g+p+r
                


        