class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=min(nums)
        right=sum(nums)
        def possible(limit):
            cur_sum=0
            partition=0
            for i in nums:
                cur_sum+=i
                if cur_sum>limit:
                    partition+=1
                    cur_sum=i
                    if cur_sum>limit:
                        return False
           
            # print(limit,partition)
            return partition<=k-1


        answer=left
        while left<=right:
            mid=(left+right)//2
            if possible(mid):
                right=mid-1
                answer=mid
            else:
                left=mid+1

        return answer
        