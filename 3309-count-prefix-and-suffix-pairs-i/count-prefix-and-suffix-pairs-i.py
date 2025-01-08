class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isprefixandsuffix(a,b):
            n=len(a)
            if a==b[:n] and a==b[-n:]:
                return True
            return False
        
        
        result=0
        for i in range(len(words)):
            for j in range(i,len(words)):
                if i!=j:
                    if isprefixandsuffix(words[i],words[j]):
                        result+=1
        return result

        