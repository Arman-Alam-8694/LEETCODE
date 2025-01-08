class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # def isprefixandsuffix(a,b):
        #     n=len(a)
        #     return a==b[:n] and a==b[-n:]
        
        # result=0
        # for i in range(len(words)):
        #     for j in range(i+1,len(words)):
        #             if isprefixandsuffix(words[i],words[j]):
        #                 result+=1
        # return result



        result=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                    if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                        result+=1
        return result
        