class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        maxx=0
        for i in range(24):
            count=0
            for num in candidates:
                if (num&(1<<i)):
                    count+=1
            maxx=max(maxx,count)

        return maxx
        