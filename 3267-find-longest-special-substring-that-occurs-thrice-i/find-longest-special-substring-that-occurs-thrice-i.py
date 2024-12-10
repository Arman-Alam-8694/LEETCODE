class Solution:
    def maximumLength(self, s: str) -> int:
        def check(k,s):
            # stringg="abcdefghijklmnopqrstuvwxyz"
            for ch in stringg:
                left=0
                tcount=0
                count=0
                right=0
                while right<len(s):
                    if s[right]==ch:
                        tcount+=1
                    if s[right]!=ch:
                        tcount=0
                        left=right+1
                    while tcount>k:
                        tcount-=1
                        left-=1
                    if tcount!=0 and tcount%k==0:
                        count+=1
                    if count==3:
                        return True

                    right+=1
            return False

        sset=set(s)
        stringg=""
        for i in sset:
            stringg+=i

        answer=-1
        n=len(s)
        left=1
        right=n
        while left<=right:
            mid=(left+right)//2
            if check(mid,s):
                answer=max(mid,answer)
                left=mid+1
            else:
                right=mid-1
        return answer

        