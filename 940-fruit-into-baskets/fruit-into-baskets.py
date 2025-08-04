class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result=0
        mapp=defaultdict(int)
        left=0
        n=len(fruits)
        counts=0
        for right in range(n):
            mapp[fruits[right]]+=1
            counts+=1
            while len(mapp)>2:
                mapp[fruits[left]]-=1
                counts-=1
                if mapp[fruits[left]]==0:
                    del mapp[fruits[left]]
                left+=1
            result=max(result,counts)
        return result
        