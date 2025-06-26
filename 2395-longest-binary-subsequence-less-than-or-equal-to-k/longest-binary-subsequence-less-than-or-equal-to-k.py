class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        #BINARY SEARCH OVER THE ANSWER WHICH IS HERE THE LENGTH OF THE SUBSEQUENCE

        # n = len(s)
        # def possible(x):
        #     to_remove=n-x
        #     val=0
        #     for i in s:
        #         if i=="1" and to_remove>0:
        #             to_remove-=1
        #         else:
        #             val=(val<<1)+int(i)
        #             if val>k:
        #                 return False

        #     return True

        # l,r=0,n
        # answer=0
        # while l<=r:
        #     mid=(l+r)//2
        #     if possible(mid):
        #         l=mid+1
        #         answer=mid
        #     else:
        #         r=mid-1

        # return answer

        count = 0
        sm=0
        bits=k.bit_length()
        for i,b in enumerate(s[::-1]):
            if b=="1":
                if sm+(1<<count)<=k:
                    sm=sm+(1<<count)
                    count+=1
            else:
                count+=1
        return count
