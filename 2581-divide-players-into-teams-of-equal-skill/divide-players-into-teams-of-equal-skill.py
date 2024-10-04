class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        count=Counter(skill)
        target=sum(skill)//(len(skill)//2)
        #we need to find a target value such that all teams sum up to this value 
        #for this we can do the total sum of all the players(array) 
        #divide it by n/2 teams this will give a number
        #which all teams can have equal other number is not possible
        #after this we iterate through the dictionary and see the 
        #frequency of curr and target-curr if it's equal we can form a pair
        #add this to the result along with it's frequency do count the duplicates
        #if frequency if not equal that means it's just not possible return -1
        result=0
    
        for k,v in count.items():
            if v!=count[target-k]:
                return -1
            result+=(k*(target-k))*v
        return result//2
        
