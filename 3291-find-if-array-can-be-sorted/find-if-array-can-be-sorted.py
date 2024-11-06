class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # sortedd=True
        # n=len(nums)
        # for i in range(n-1):
        #     if not nums[i]<=nums[i+1]:
        #         sortedd=False
        #         break
        # if sortedd==True:
        #     return True
          
        # dictt={}
        # for i in nums:
        #     count=0
        #     for j in range(0,11):
        #         if 1<<j&i:
        #             count+=1
        #     dictt[i]=count
        # print(dictt)
        # while True:
        #     sortedd=True
        #     change=False
        #     for i in range(len(nums)-1):
        #         if nums[i]>nums[i+1]:
        #             if dictt[nums[i]]==dictt[nums[i+1]]:
        #                 nums[i],nums[i+1]=nums[i+1],nums[i]
        #                 change=True
        #                 if i!=0 and nums[i]<nums[i-1]:
        #                     sortedd=False

        #             else:
        #                 sortedd=False
        #     if sortedd:
        #         return True
        #     else:
        #         if change==False:
        #             return False
        def bitscount(i):
            count=0
            for j in range(0,11):
                if 1<<j&i:
                    count+=1
            return count


        sortedd=True
        n=len(nums)
        for i in range(n-1):
            if not nums[i]<=nums[i+1]:
                sortedd=False
                break
        if sortedd==True or n==1:
            return True
        result=[]
        dictt={}
        prev=None
        minn=-1
        maxx=-1
        for i in range(n):
            digit=nums[i]
            bits=bitscount(digit)
            if not prev:
                minn,maxx=digit,digit
            elif prev and prev==bits:
                if digit<minn:
                    minn=digit
                elif digit>maxx:
                    maxx=digit
            elif prev and prev!=bits:
                result.append([minn,maxx])
                minn,maxx=digit,digit
            prev=bits
        result.append([minn,maxx])
        for i in range(len(result)-1):
            if not result[i][1]<result[i+1][0]:
                return False

        return True






    
        