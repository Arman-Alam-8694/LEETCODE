class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        answer=0
        left,right=0,1
        n=len(nums)
        prev=False
        for i in range(1,n-1):
            if nums[i] == nums[i - 1]:
                continue
            if right<i:
                right=i+1
            while nums[i-1]!=nums[i] and right<n:
                if nums[right]!=nums[i]:
                    break
                right+=1
        
            if nums[i-1]!=nums[i] and left<i and i<right and right<n:
                # print(left,i,right)
                # print(nums[left],nums[i],nums[right])
                if (nums[left]>nums[i] and nums[right]>nums[i]) or (nums[left]<nums[i] and nums[right]<nums[i]):
                    # print(nums[left],nums[i],nums[right])
                    answer+=1
                left=i
        return answer


        