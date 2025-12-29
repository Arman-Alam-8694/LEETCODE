class Solution:
    def removeDigit(self, num: str, d: str) -> str:
        n = len(num)
        listt=[]

        for i in range(n):
            if num[i] == d:
                listt.append(num[:i]+num[i+1:])

        return max(listt)
            