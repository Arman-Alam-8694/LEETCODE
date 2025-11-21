class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars=set(s)
        
        answer=0
        done=set()
        for i in chars:
            new=set()
            Found=False
            for j in range(len(s)):
                if s[j]==i and Found:
                    
                    if len(new)!=0:
                        done.update(new)
                        new=set()
                        new.add(i)
                    else:
                        new.add(i)
                    
                elif s[j]==i:
                    Found=True
                elif Found:
                    if s[j] not in done:
                        new.add(s[j])
            answer+=len(done)
            done=set()
        return answer


                    






        