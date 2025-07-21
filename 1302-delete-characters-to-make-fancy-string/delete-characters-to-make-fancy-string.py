class Solution:
    def makeFancyString(self, s: str) -> str:
        answer=[s[0]]
        prev=None
        cnt=0
        for i in s:
            cnt+=1
            if prev is not None:
                if i==prev and cnt==3:
                    cnt-=1

                elif i!=prev:
                    answer.append(i)
                    prev=i
                    cnt=1
                else:
                    answer.append(i)
            else:
                prev=i

        return "".join(answer)
        