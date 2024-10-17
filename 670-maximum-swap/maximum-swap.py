class Solution:
    def maximumSwap(self, num: int) -> int:
        digits=list(str(num))
        sl,sr=0,0
        n=len(digits)-1
        r=n
        for l in range(n,-1,-1):
            if digits[l]>digits[r]:
                r=l
            elif digits[l]<digits[r]:
                sl,sr=l,r
        digits[sl],digits[sr]=digits[sr],digits[sl]
        return int("".join(digits))
        
