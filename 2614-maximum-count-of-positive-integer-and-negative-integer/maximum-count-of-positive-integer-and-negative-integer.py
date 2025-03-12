class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        maxx=0
        n=len(nums)
        def binSearch():
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                # print(mid)
                if nums[mid]<0:
                    left=mid+1
                else:
                    right=mid-1
            return left

        def binSearchh():
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                # print(mid)
                if nums[mid]<=0:
                    left=mid+1
                else:
                    right=mid-1

            # print(left)
            return 0 if left==len(nums) else len(nums)-left

        return max(binSearch(),binSearchh())


