class Solution:
    def checkValidCuts(self, n: int, A: List[List[int]]) -> bool:
        def check(A):
            res = 0
            A.sort()
            pre = A[0][1]
            for a,b in A:
                res += pre <= a
                pre = max(pre, b)
            return res > 1

        return check([a[::2] for a in A]) or check([a[1::2] for a in A])
        