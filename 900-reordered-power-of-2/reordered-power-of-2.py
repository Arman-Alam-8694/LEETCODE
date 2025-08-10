class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def check(x):
            return (x&(x-1))==0
        if check(n):
            return True

        listt=[i for i in str(n)]
        used=[False]*len(listt)

        def backtrack(formed):
            if len(formed)==len(listt):
                if check(int(''.join(formed))):
                    return True
                return False

            for i in range(len(listt)):
                if used[i]:
                    continue

                if len(formed)==0 and listt[i]=="0":
                    continue
                formed.append(listt[i])
                used[i]=True
                if backtrack(formed):
                    return True
                formed.pop()
                used[i]=False
            return False

        return backtrack([])



        # def recur()