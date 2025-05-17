class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # """
        
        
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[j] < nums[i]:
        #             print(nums[j],nums[i])
        #             nums[i], nums[j] = nums[j], nums[i]
        
        # insert0 = 0  # Where the next 0 should go
        # insert1 = 0  # Where the next 1 should go (after 0s)

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         # Shift right from insert0 to i
        #         temp = nums[i]
        #         for j in range(i, insert0, -1):
        #             nums[j] = nums[j - 1]
        #         nums[insert0] = temp
        #         insert0 += 1
        #         insert1 += 1  # 1s shift forward due to inserted 0
        #     elif nums[i] == 1:
        #         # Shift right from insert1 to i
        #         temp = nums[i]
        #         for j in range(i, insert1, -1):
        #             nums[j] = nums[j - 1]
        #         nums[insert1] = temp
        #         insert1 += 1

        n=len(nums)
        low,mid=0,0
        high=n-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
