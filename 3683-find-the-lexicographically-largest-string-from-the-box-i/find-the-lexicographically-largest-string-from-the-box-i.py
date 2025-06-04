class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        max_string=[]
        def get_rank(a):
            return ord(a)-ord("a")
        n=len(word)
        max_contain=n-((numFriends)-1)

        for i in range(n):
            temp=0
            tlist=[]
            smaller=False
            while temp<len(max_string):
                # print("here")
                # print(i+temp)
                if i+temp>=n:
                    smaller=True
                    break
                rank1=get_rank(word[i+temp])
                rank2=get_rank(max_string[temp])
                if rank1==rank2:
                    tlist.append(word[i+temp])
                    temp+=1
                elif rank1<rank2:
                    smaller=True
                    break
                else:
                    break
   

            if not smaller:
                while i+temp<n and temp<max_contain:
                    tlist.append(word[i+temp])
                    temp+=1
            # print(tlist)
            if not smaller:
                max_string=tlist.copy()

        return "".join(max_string)

        