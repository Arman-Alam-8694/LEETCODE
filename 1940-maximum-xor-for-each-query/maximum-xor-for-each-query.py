class Solution:
    def getMaximumXor(self, nums, maximumBit):
        # def getmax(tmax,maxx):
        #     # nmax=0
        #     # temp=""
        #     # move=0
        #     # # print(tmax)
        #     # # print("tmax",bin(tmax))
        #     # while True:
        #     #     if tmax&(1<<move):
        #     #         temp+="0"
        #     #     else:
        #     #         temp+="1"
        #     #     # print(temp)
        #     #     comp=int(temp[::-1],2)
        #     #     # print(comp)
        #     #     if comp>=maxx:
        #     #         break
        #     #     else:
        #     #         nmax=comp
        #     #     move+=1
        #     comp=int(bin(~tmax)[3:],2)
        #     return min(comp,maxx-1)
       
        # total_xor=0
        # for i in nums:
        #     total_xor^=i
        # result=[]
        # maxx=2**(maximumBit)
        # result.append(getmax(total_xor,maxx))
        # for i in range(-1,-1*(len(nums)),-1):
        #     total_xor^=nums[i]
        #     # print(total_xor)
        #     result.append(getmax(total_xor,maxx))
        # # result.append(getmax(total_xor,maxx))
        # return result
        result=[]
        mask=(1<<maximumBit)-1
        xor=0
        for i in nums:
            xor^=i
            result.append(xor^mask)
        return result[::-1]

        