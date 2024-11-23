class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows=len(box)
        cols=len(box[0])
        row=rows-1
        result=[["."]*rows for _ in range(cols)]
        
        for i in range(rows):
            candidaterow=None
            candidatecol=None

            place=None
            for j in range(cols):
                result[j][row-i]=box[i][j]
            
                if box[i][j]=="#" and (candidaterow==None and candidatecol==None):
                    candidaterow=i
                    candidatecol=j
                elif box[i][j]==".":
                    if candidaterow!=None and candidatecol!=None:
    
                        result[j][row-i]="#"
                        result[candidatecol][row-candidaterow]="."
                        candidatecol+=1
                elif box[i][j]=="*":

                    candidaterow=None
                    candidatecol=None
                
        return result
            