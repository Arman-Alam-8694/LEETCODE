class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        sortt=sorted(intervals,key=lambda a:(a[1],-a[0]))
        answer=0
        a,b=-1,-1
        for i in sortt:
            if a==-1 and b==-1:
                a=i[1]-1
                b=i[1]
                answer+=2
            else:
                if (i[0]<=a<=i[1]) and (i[0]<=b<=i[1] ):
                    continue

                elif (not i[0]<=a<=i[1]) and (not i[0]<=b<=i[1] ):
                    a=i[1]-1
                    b=i[1]
                    answer+=2

                    
                
                
                elif i[1]==b:
            
                    a=i[1]-1
                    answer+=1
                else:
                    temp=b
                    b=i[1]
                    a=temp
                    answer+=1
                    

                    

                
       
        return answer
        