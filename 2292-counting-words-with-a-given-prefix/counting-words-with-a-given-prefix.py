class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        a=len(pref)
        result=0
        for i in words:
            if i[:a]==pref:
                result+=1
        return result