class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        res=0
        MOD=10**9+7
     
        temp=[0]*26
        for i in s:
            temp[ord(i)-ord("a")]+=1
        queue=deque(temp)
        # for rounds in range(t):
        #     next=[0]*26
        #     for i in range(0,26):
        #         if temp[i]>0:
        #             if i==25:
        #                 next[0]+=temp[i]
        #                 next[1]+=temp[i]
                        
        #             else:
        #                 next[i+1]+=temp[i]
        #     # print(next)
        #     temp=next
        # return sum(temp)%MOD


        #USING DEQUE simulation kind of thing we pop the z and add it to a counts
        #to make final b counts and then just pop the z one and appendleft to form the
        #new A counts and by doing so we have shifted the counts of each char to char+1 
        #hence effectively simmulating as well compared to upper brute force of 
        #additional O(26) at each t 
        for i in range(t):
            queue[0]+=queue[25]
            queue.appendleft(queue.pop())
        return sum(queue)%MOD


