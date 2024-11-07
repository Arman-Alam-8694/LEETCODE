import sys
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stringg=str(n)
        largest=float("-inf")
        # a=list(map(int,str(n)))
        # b=sorted(a)
        # if b==a:
            


        
        for i in range(-1,-1*(len(stringg)+1),-1):
            if int(stringg[i])>=largest:
                largest=int(stringg[i])
            else:
                tstring=""
                temp=sorted(list(map(int,stringg[i+1:])))
                minn=-1
                # print(temp)
                for j in temp:
                    if j>int(stringg[i]):
                        minn=j
                        break
                if minn==-1:
                    return -1
                tstring+=str(minn)
                temp.remove(minn)
                temp.append(int(stringg[i]))
                temp.sort()
                # print(temp)
                temp=list(map(str,temp))
                tstring+="".join(temp)
                result=int(stringg[:i]+tstring)
                if result>2**31-1:
                    return -1
                return result
        return -1

            