class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes=list(map(int,boxes))
        mapp={}
        n=len(boxes)
        for i in range(n):
            if boxes[i]>0:
                mapp[i]=boxes[i]
        result=[]
        for i in range(n):
            total=0
            for idx,val in mapp.items():
                if idx!=i:
                    total+=abs(i-idx)*val
            result.append(total)
        return result
        