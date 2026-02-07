class Solution:
    def minimumDeletions(self, s: str) -> int:
        nxt_found=0
        nxt_notfound=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="a":
                curr_found=1+nxt_found
                curr_notfound=nxt_notfound
            else:
                curr_found=nxt_found
                curr_notfound=min(1+nxt_notfound,nxt_found)
            nxt_found,nxt_notfound=curr_found,curr_notfound
        return min(nxt_found,nxt_notfound)


        