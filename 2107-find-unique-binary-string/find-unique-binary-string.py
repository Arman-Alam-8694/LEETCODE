class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        lookup=set(nums)
        n=len(nums)

        def backtrack(listt,lookup):
            if len(listt)==n:
                stringg="".join(listt)
                if stringg in lookup:
                    return False
                else:
                    return stringg


            for i in ("0","1"):
                listt.append(i)
                res=backtrack(listt,lookup)
                if not res:
                    listt.pop()
                else:
                    return res

        return backtrack([],lookup)
                
        