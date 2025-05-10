class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # res=set()
        # n=len(digits)
        # for i in range(n):
        #     temp=[str(digits[i])]
        #     if temp==["0"]:
        #         temp.pop()
        #         continue
        #     for j in range(n):
        #         temp.append(str(digits[j]))
        #         for k in range(n):
        #             temp.append(str(digits[k]))
        #             if not(i==j or j==k or k==i):
        #                 if int("".join(temp))%2==0:
        #                     res.add(int("".join(temp)))
        #             temp.pop()
        #         temp.pop()
        #     temp.pop()
        # return sorted(res)

        result=[]
        mapp=Counter(digits)
        for i in range(100,1000):
            temp=defaultdict(int)
            b=i
            if i%2==0:
                while i!=0:
                    a=i%10
                    temp[a]+=1
                    i=i//10
                found=True
                for i,j in temp.items():
                    if mapp[i]<j:
                        found=False
                        break
                if found:
                    result.append(b)
        return result
                    


                        
        