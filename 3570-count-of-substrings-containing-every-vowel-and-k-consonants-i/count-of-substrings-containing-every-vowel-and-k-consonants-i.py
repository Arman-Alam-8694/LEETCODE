class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel=0
        cons=0
        size=5+k
        n=len(word)
        vow=["a","e","i","o","u"]
        vow_map={}
        temp=0
        tvow={}
        left=0
        result=0
        for right in range(n):
            if word[right] in vow:
                if word[right] not in vow_map:
                    vow_map[word[right]]=0
                vow_map[word[right]]+=1
                if word[right] not in tvow:
                    tvow[word[right]]=0
                tvow[word[right]]+=1
                if len(tvow)==5 and tcons==k:
                    while temp<right and len(tvow)==5 and tcons==k:
                        if word[temp] in vow:
                            tvow[word[temp]]-=1
                            if tvow[word[temp]]==0:
                                del tvow[word[temp]]
                        else:
                            tcons-=1
                        temp+=1
            
            else:
                cons+=1
         
            
            while cons>k:
                if word[left] in vow:
                    vow_map[word[left]]-=1
                    if vow_map[word[left]]==0:
                        del vow_map[word[left]]
                else:
                    cons-=1
                left+=1
            if temp<=left:
                tcons=cons
                tvow=vow_map.copy()
                temp=left
                while temp<right and len(tvow)==5 and tcons==k:
                    if word[temp] in vow:
                        tvow[word[temp]]-=1
                        if tvow[word[temp]]==0:
                            del tvow[word[temp]]
                    else:
                        tcons-=1
                    temp+=1
            
            if temp>left:
           
                result+=(temp-left)



        # print(left,right)
        # while cons==k and len(vow_map)==5:
        #     if word[left] in vow:
        #         vow_map[word[left]]-=1
        #         if vow_map[word[left]]==0:
        #             del vow_map[word[left]]
        #     else:
        #         cons-=1
        #     left+=1
        #     if len(vow_map)==5 and cons==k:
        #         result+=1


        return result

        