class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        start,end=0,10**9+1
        total_area=0
        n=len(squares)
        for i in range(n):
            x,y,l=squares[i]
            total_area+=l*l
        target=total_area/2.0

        while end-start>1e-6:
            mid=(start+end)/2
            tarea=0.0
            for x,y,l in squares:
                if mid<=y:
                    continue
                elif mid>=(y+l):
                    tarea+=(l*l)
                else:
                    tarea+=(mid-y)*l
            if tarea<target:
                start=mid
            else:
                end=mid

        return start
