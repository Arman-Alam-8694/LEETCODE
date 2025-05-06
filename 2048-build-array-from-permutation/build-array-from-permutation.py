class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # result=[]
        # for i in range(len(nums)):
        #     result.append(nums[nums[i]])
        # return result

        # modifying the array
        for i in range(len(nums)):
            nums[i]+=1000*(nums[nums[i]]%1000)
        for i in range(len(nums)):
            nums[i]=nums[i]//1000
        return nums
        