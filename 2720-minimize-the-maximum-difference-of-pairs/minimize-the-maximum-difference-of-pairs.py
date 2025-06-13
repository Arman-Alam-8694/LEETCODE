class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        # print(nums)
        # answer=float("inf")
        n=len(nums)
        # left=0
        # right=n-1
        # found=0
        # tleft=0
        # tright=n-1
        # while left<=right and found<p:
        #     left_part=nums[left+1]-nums[left]
        #     right_part=nums[right]-nums[right-1]
        #     if left_part<right_part:
        #         answer=min(answer,left_part)
        #         left+=2
        #     else:
        #         answer=min(answer,right_part)
        #         right-=2
        #     found+=1

        # return answer
        def check(x):
            idx=0
            found=0
            while idx<n-1:
                if nums[idx+1]-nums[idx]<=x:
                    found+=1
                    idx+=1
                idx+=1
            return found

        left=0
        right=nums[-1]-nums[0]
        while left<=right:
            mid=(left+right)//2
            if check(mid)>=p:
                right=mid-1
            else:
                left=mid+1
        return left
        