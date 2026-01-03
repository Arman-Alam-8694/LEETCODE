class Solution:
    def numOfWays(self, n: int) -> int:
        mod=10**9+7
    
        two=6
        three=6
        ans=0
        for i in range(1,n):
            nthree=0
            ntwo=0
            if two:
                ntwo+=(two*3)%mod
                nthree+=(two*2)%mod
                # print(ntwo,nthree)
            if three:
                ntwo+=(three*2)%mod
                nthree+=(three*2)%mod
                # print(ntwo,nthree)
            two=ntwo
            three=nthree
            # print("atlast",two,three)

        return (two+three)%mod

        