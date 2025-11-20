class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        sortt=sorted(intervals,key=lambda a:a[1])
        answer=[]
        a,b=-1,-1
        print(sortt)
        for i in sortt:
            if a==-1 and b==-1:
                a=i[1]-1
                b=i[1]
                answer.append(a)
                answer.append(b)
            else:
                if (not i[0]<=a<=i[1]) and (not i[0]<=b<=i[1] ):
                    a=i[1]-1
                    b=i[1]
                    answer.append(a)
                    answer.append(b)

                    
                
                elif (not i[0]<=a<=i[1]) and i[1]!=b:
                    temp=b
                    b=i[1]
                    a=temp
                    answer.append(b)
                elif (not i[0]<=a<=i[1]) and i[1]==b:
            
                    a=i[1]-1
                    answer.append(a)
                    

                    

                
        print(answer)
        return len(answer)
        