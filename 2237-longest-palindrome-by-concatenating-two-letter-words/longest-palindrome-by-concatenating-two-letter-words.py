class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        result=0
        mapp={}
        sett=set()
        for i,w in enumerate(words):
            rev=w[::-1]
            same=False
            if rev==w:
                same=True
            if rev in mapp:
                result+=4
                mapp[rev]-=1
                if mapp[rev]==0:
                    if same and rev in sett:
                        sett.remove(rev)
                    del mapp[rev]
            else:
                if w not in mapp:
                    mapp[w]=0
                if same:
                    sett.add(rev)
                mapp[w]+=1
        # print(sett)
        return result if len(sett)==0 else result+2
    
        