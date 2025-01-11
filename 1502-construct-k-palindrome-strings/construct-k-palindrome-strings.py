class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # if k>len(s):
        #     return False
        # if k==len(s):
        #     return True
        # mapp=Counter(s)
        # odd_count,even_count=0,0
        # odd_sum,even_sum=0,0
        # for i,v in mapp.items():
        #     if v&1:
        #         odd_count+=1
        #         odd_sum+=v
        #     else:
        #         even_sum+=v
        # if odd_count>k:
        #     return False
        # if odd_count==k:
        #     return True
        # if odd_sum>=k :
        #     return True
        # if odd_sum<=k:
        #     if (k-odd_sum)<=even_sum:
        #         return True
            
        # return False


        if k>len(s):
            return False
        # if k==len(s):
        #     return True
        odd_count=0
        for i in set(s):
            if s.count(i)&1:
                odd_count+=1
        if odd_count>k:
            return False
        return True
           
        


 