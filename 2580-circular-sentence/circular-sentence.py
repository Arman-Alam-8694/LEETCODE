class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        listt=sentence.split()
        n=len(listt)
        for i in range(n):
            if listt[i][-1]!=listt[(i+1)%n][0]:
                return False
        return True
        