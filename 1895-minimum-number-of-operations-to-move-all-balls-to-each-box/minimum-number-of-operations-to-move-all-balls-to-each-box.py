class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        mapp={}
        n=len(boxes)
        for i in range(n):
            val=int(boxes[i])
            if val>0:
                mapp[i]=val
        result=[]
        for i in range(n):
            total=0
            for idx,val in mapp.items():
                if idx!=i:
                    total+=abs(i-idx)*val
            result.append(total)
        return result
        