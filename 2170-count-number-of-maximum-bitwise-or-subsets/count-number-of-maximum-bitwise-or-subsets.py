class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or=0
        for i in nums:
            max_or|=i


        print(max_or)
        counts=0
        n=len(nums)
        def recur(idx,cur_cal,max_or):
            nonlocal counts
            
            if idx>=n:
                if cur_cal==max_or:
                    # print('jdoifd')
                    counts+=1
                return 
            
            recur(idx+1,cur_cal,max_or)
            recur(idx+1,cur_cal|nums[idx],max_or)


        recur(0,0,max_or)
        return counts
        

        