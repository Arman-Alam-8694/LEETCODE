class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mapp=Counter(nums)
        for k,v in mapp.items():
            if v&1:
                return False
        return True

        