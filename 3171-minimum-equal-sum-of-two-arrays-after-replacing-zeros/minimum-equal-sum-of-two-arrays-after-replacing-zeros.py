class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        fzero,szero,fsum,ssum=0,0,0,0
        for i in nums1:
            if i==0:
                fzero+=1
        
            fsum+=i
        for j in nums2:
            if j==0:
                szero+=1
        
            ssum+=j

        print(fsum,fzero)
        print(ssum,szero)
        if fsum>ssum:
            fhas=fsum-ssum
            if fhas+fzero>=szero and szero!=0:
                return fzero+fsum
            elif szero>=fhas+fzero and fzero!=0:
                return szero+ssum
            else:
                return -1
        elif fsum==ssum:
            if fzero==0 and szero==0:
                return fsum
            if fzero==0 or szero==0:
                return -1
            return max(fzero,szero)+fsum

        else:
            shas=ssum-fsum
            if shas+szero>=fzero and fzero!=0:
                return szero+ssum
            elif szero!=0 and fzero>=shas+szero:
                return fsum+fzero
            else:
                return -1

            
        