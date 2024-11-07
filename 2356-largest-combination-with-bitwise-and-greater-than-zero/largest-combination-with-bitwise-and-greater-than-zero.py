class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        maxx=0
        mask=1
        for i in range(24):
            count=0
            for num in candidates:
                if num&mask:
                    count+=1
            maxx=max(maxx,count)
            mask<<=1
          

        return maxx
        