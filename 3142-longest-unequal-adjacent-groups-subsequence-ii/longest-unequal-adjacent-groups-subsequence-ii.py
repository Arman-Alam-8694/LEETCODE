class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n=len(words)
        def checkhamming(first,second):
            cnt=0
            
            for i in range(len(first)):
                if second[i]!=first[i]:
                    cnt+=1
                if cnt>1:
                    return False
            return cnt==1
        result=[]
        @cache
        def recur(prev,curidx):
            take=[]
            if curidx==n:
                return []
            skip=recur(prev,curidx+1)
            if prev==-1:
                take=[words[curidx]]+recur(curidx,curidx+1)
               
            elif len(words[prev])==len(words[curidx]):
                check=checkhamming(words[prev],words[curidx])
                if check and groups[prev]!=groups[curidx]:
                    take=[words[curidx]]+recur(curidx,curidx+1)
            
            if len(take)>len(skip):
                return take
            else:
                return skip

        return recur(-1,0)


        