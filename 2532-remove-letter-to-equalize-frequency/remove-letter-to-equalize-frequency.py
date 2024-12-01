class Solution:
    def equalFrequency(self, word: str) -> bool:
        mapp={}
        n=len(word)
        lowest=n*2
        highest=0
        highest_count=0
        for i in word:
            if i in mapp:
                mapp[i]+=1
            else:
                mapp[i]=1
            highest=max(highest,mapp[i])
        lowest=min(list(mapp.values()))
        highest_count=list(mapp.values()).count(highest)
        lowest_count=list(mapp.values()).count(lowest)
        # print(len(set(mapp.values())))
        print(highest,lowest)
        print(highest_count,lowest_count)
        if highest==lowest:
            if highest!=1:
                if len(set(word))==1:
                    return True
                return False
            return True
        elif len(set(mapp.values()))!=2:
            return False
        elif (highest-lowest)!=1:
            if lowest_count==1 and lowest==1:
                return True
            return False
        if highest_count>1:
            if lowest==1 and lowest_count==1:
                return True
            return False
        return True
        