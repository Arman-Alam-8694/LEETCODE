class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        count=Counter(skill)
        target=sum(skill)//(len(skill)//2)
        result=0
    
        for k,v in count.items():
            if v!=count[target-k]:
                return -1
            result+=(k*(target-k))*v
        return result//2
        