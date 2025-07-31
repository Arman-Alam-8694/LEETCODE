class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()      # all ORs seen so far
        cur = set()      # ORs of subarrays ending at previous index
        for x in arr:
            # new ORs ending at this element:
            nxt = {x} | {x | y for y in cur}
            res |= nxt
            cur = nxt
        return len(res)


        