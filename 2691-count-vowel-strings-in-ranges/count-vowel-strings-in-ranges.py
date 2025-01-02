class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(words)
        pref_cnt=[0]*(n+1)
        result=[]
        cnt=0
        for i,word in enumerate(words):
            if (word[0] in "aeiou") and (word[-1] in "aeiou"):
                cnt+=1
            pref_cnt[i+1]=cnt
   
        for x,y in queries:
            result.append(pref_cnt[y+1]-pref_cnt[x])
        return result



        