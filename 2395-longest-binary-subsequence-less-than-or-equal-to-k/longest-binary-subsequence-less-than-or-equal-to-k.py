class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        #BINARY SEARCH OVER THE ANSWER WHICH IS HERE THE LENGTH OF THE SUBSEQUENCE

        n = len(s)
        def possible(x):
            to_remove=n-x
            val=0
            for i in s:
                if i=="1" and to_remove>0:
                    to_remove-=1
                else:
                    val=(val<<1)+int(i)
                    if val>k:
                        return False

            return True

        l,r=0,n
        answer=0
        while l<=r:
            mid=(l+r)//2
            if possible(mid):
                l=mid+1
                answer=mid
            else:
                r=mid-1

        return answer