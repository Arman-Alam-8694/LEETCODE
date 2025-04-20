class Solution:
    def numRabbits(self, answers: List[int]) -> int:


        # so in this the only trick part is knowing how will group the rabbits
        #for example if rabbit i says i have seen 3 rabbits that means at least there are 4 rabbits
        #of same kind right,so the moment we find 4 rabbits to say the same number that means the group
        #is completed right, the moment we encounter i+1 times rabbit saying the same number i that
        #group is completed, we have to then again start the same procedure when we encounter the same
        #number right for example 1 1 1 - when you are index 1 you know you have seen the same group 
        #but then you find another same rabbit saying the same number this could only mean a new 
        #rabbit type so we start the same procedure again 
        #if the type of rabbit is not found then we do simple result+=(i+1) until i+1 has rabbits says
        #the same number right for 0 we remove it just after because we have found 0+1 saying the 
        #same number 


        n=len(answers)
        mapp={}
        result=0
        for i in answers:
            if i not in mapp:
                result+=(i+1)
                mapp[i]=1
            else:
                mapp[i]+=1
            if mapp[i]==i+1:
                del mapp[i]
        return result


        