class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        #bruteforce O(1) space complexity
        # current=0
        # n=len(derived)
        # for i in range(n):
        #     if i==n-1:
        #         if 0^current==derived[i]:
        #             return True
        #         else:
        #             return False
        #     else:
        #         current^=derived[i]

        #optimised observation O(1) space complexity
        # n=len(derived)
        # cnt=derived.count(1) if derived[n-1]!=1 else derived.count(1)-1
        # if cnt&1:
        #     if derived[n-1]==1:
        #         return True
        #     else:
        #         return False
        # else:
        #     if derived[n-1]==0:
        #         return True
        #     else:
        #         return False

        #simplified observation
        return sum(derived)%2==0
                
