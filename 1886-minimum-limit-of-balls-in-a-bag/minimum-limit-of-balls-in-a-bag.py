class Solution:
    def minimumSize(self, nums: List[int], O: int) -> int:
        N = len(nums)
        S = sum(nums)
        G = N+O
        if G >= S: return 1

        def verify(v):
            return sum(math.ceil(n/v) for n in nums) <= G
        
        l = math.ceil(S/G)-1
        h = min(max(nums),math.floor(S/O))
        
        while l<h-1:
            m = (h+l)//2
            if verify(m): h=m
            else: l=m
        return h