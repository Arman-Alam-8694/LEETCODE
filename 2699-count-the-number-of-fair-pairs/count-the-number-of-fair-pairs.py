

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0

        def helper(nums,target):
            left=0
            right=n-1
            temp=0
            while left<right:
                if nums[left]+nums[right]<target:
                    left+=1
                else:
                    temp+=right-left
                    right-=1
            return temp
        # def bisect_left(num, start):
        #     low, high = start, n - 1
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if nums[mid] < num:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        #     return low

        # def bisect_right(num, start):
        #     low, high = start, n - 1
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if nums[mid] <= num:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        #     return low

        # for i in range(n):
        #     low = lower - nums[i]
        #     high = upper - nums[i]
        #     left = bisect_left(low, i + 1)
        #     right = bisect_right(high, i + 1)
        #     res += right - left

        # return res
        res=helper(nums,lower)-helper(nums,upper+1)
        return res



