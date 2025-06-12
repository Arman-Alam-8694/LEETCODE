class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        #didn't get in the first attempt good question to code again 
        #the hint was in the constraint that's why i think this is little 
        #bit of different problem compared to others, once i did notice that 
        #but thought of doing it very optimal way which was messier that time
        #so that's couldn't think of just going by making couples of different
        #numbers and try it linearly 

        #for this question the time complexity will O(2On)
        #there total total 5*4 unique pairs so yeh 20 times linear
        #which is doable but not easy to go that path you know

        #let's go and i got the idea of prefix sum and all as well 
        #in the first time but still couldn't solve this question 
        
        #BECAUSE I WAS NOT GOING STEP BY STEP , I WAS TRYING TO HANDLE
        #LOT OF CASES IN JUST ONE PASS SO THAT'S WHAT MADE ME LOSE SO MUCH 
        # AND HENCE THE INTEREST AS WELL    

        n=len(s)
        ans=float("-inf")
        pairs=["0","1","2","3","4"]


        def get_status(ca,cb):
            return (ca&1)<<1|(cb&1)

        for a in pairs:
            for b in pairs:
                if a==b:
                    continue
                #there are four states in terms of odd and even 
                #00 01 10 11
                best=[float("inf")]*4
                left=-1
                cnt_a,cnt_b=0,0
                prev_a,prev_b=0,0
                for right in range(n):
                    cnt_a+=s[right]==a
                    cnt_b+=s[right]==b
                    while right-left>=k and cnt_b-prev_b>=2:
                        ll=get_status(prev_a,prev_b)
                        best[ll]=min(best[ll],prev_a-prev_b)
                        left+=1
                        prev_a+=s[left]==a
                        prev_b+=s[left]==b
                    rr=get_status(cnt_a,cnt_b)
                    if best[rr^0b10]!=float("inf"):
                        ans=max(ans,cnt_a-cnt_b-best[rr^0b10])

        return ans

