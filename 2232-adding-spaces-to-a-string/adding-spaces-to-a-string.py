class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer=""
        start=0
        space=0
        while start<len(s):
            if space<len(spaces) and spaces[space]==start:
                answer+=" "
                space+=1
                continue
            else:
                answer+=s[start]

            start+=1
        return answer