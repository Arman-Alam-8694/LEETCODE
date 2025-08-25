class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row=len(mat)
        col=len(mat[0])
        start=[0,0]
        answer=[]
        count=0
        total=row*col
        while count<total:
            while True:
                curr=start[0]
                curc=start[1]
                answer.append(mat[curr][curc])
                count+=1
                nextr=curr-1
                nextc=curc+1
                start=[nextr,nextc]
                if nextc>=col:
                    start=[nextr+2,nextc-1]
                    break
                elif nextr<0:
                    start=[nextr+1,nextc]
                    break
            
            if count>=total:
                break
            while True:
                curr=start[0]
                curc=start[1]
                answer.append(mat[curr][curc])
                count+=1
                nextr=curr+1
                nextc=curc-1
                start=[nextr,nextc]
                if nextr>=row:
                    start=[nextr-1,nextc+2]
                    break
                elif nextc<0:
                    start=[nextr,nextc+1]
                    break

        return answer

                


        