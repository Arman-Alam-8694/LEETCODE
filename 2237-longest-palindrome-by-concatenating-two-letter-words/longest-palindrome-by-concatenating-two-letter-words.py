class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        result=0
        mapp={}
        for i,w in enumerate(words):
            rev=w[::-1]
            if rev in mapp:
                result+=4
                mapp[rev]-=1
                if mapp[rev]==0:
                    del mapp[rev]
            else:
                if w not in mapp:
                    mapp[w]=0
                mapp[w]+=1

        if mapp:
            for k,v in mapp.items():
                if k==k[::-1]:
                    result+=2
                    return result
        return result
    
        