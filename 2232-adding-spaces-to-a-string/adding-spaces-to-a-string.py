class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer=[]
        start=0
        for space in spaces:
            answer.append(s[start:space])
            start=space
        answer.append(s[start:])
        return " ".join(answer)