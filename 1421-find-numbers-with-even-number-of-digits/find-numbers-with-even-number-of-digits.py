class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even=0
        # for n in nums:
        #     if not len(str(n))&1:
        #         even+=1

        # return even
        # for n in nums:
        #     cnt=0
        #     while n!=0:
        #         n//=10
        #         cnt+=1
        #     if not cnt&1:
        #         even+=1
        # return even
        for n in nums:
            if 9<n<100:
                even+=1
            elif 999<n<10000:
                even+=1
            elif 99999<n<1000000:
                even+=1
        return even


        