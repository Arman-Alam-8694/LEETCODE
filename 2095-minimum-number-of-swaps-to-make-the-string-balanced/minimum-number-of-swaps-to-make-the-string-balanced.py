class Solution:
    def minSwaps(self, s: str) -> int:
        opening=0
        closing=0
        steps=0
        for i in s:
            if i=="[":
                opening+=1
            if i=="]":
                closing+=1
            if closing>opening:
                steps+=1
                closing-=1
                opening+=1
        return steps
        