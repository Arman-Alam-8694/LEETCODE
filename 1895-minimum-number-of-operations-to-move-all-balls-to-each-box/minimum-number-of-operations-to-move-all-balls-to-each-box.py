class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        #hash map using the index and val

        # boxes=list(map(int,boxes))
        # mapp={}
        # n=len(boxes)
        # for i in range(n):
        #     if boxes[i]>0:
        #         mapp[i]=boxes[i]
        # result=[]
        # for i in range(n):
        #     total=0
        #     for idx,val in mapp.items():
        #         if idx!=i:
        #             total+=abs(i-idx)*val
        #     result.append(total)
        # return result


        #2pass O(n) using prefix and suffix and adding them up for the result
        n=len(boxes)
        res=[0]*n
        left_ball,pref=0,0
        for i,val in enumerate(boxes):
            res[i]=pref
            pref+=left_ball
            if int(val)==1:
                left_ball+=1
                pref+=1
        right_ball,suf=0,0
        for i in range(n-1,-1,-1):
            res[i]+=suf
            suf+=right_ball
            if int(boxes[i])==1:
                right_ball+=1
                suf+=1

        return res
        