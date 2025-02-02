class Solution:
    def check(self, nums: List[int]) -> bool:
        # listt="*".join(map(str,sorted(nums)))
        # list1=listt+"*"+listt
        # print(list1)
        # print(nums)
        # n="*".join(map(str,nums))
    
        # if n in list1:
        #     return True
        # return False

        cnt=0
        n=len(nums)
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                cnt+=1
            if cnt>1:
                return False
        return True

