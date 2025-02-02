class Solution:
    def check(self, nums: List[int]) -> bool:
        listt="*".join(map(str,sorted(nums)))
        list1=listt+"*"+listt
        print(list1)
        print(nums)
        n="*".join(map(str,nums))
    
        if n in list1:
            return True
        return False