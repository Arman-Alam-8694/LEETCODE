class Solution:
    
    def numTilePossibilities(self, tiles: str) -> int:
        #if the question included printing the sequences then this solution is better
        # unique_numbers=list(set(tiles))
        # available=Counter(tiles)
        # result=set()
        # def backtrack(cur_list,available,result):
        
        #     for i in unique_numbers:
        #         if available[i]>0:
        #             cur_list.append(i)
        #             stringg="".join(cur_list)
                  
        #             result.add(stringg)
                 
        #             available[i]-=1
                   
        #             backtrack(cur_list,available,result)
        #             available[i]+=1
        #             cur_list.pop()
                 

        # backtrack([],available,result)
        # return len(result)


    

        #just for numbers
        available = Counter(tiles)  
        count = 0  

        def backtrack():
            nonlocal count
            for tile in available:
                if available[tile] > 0:
                    available[tile] -= 1  
                    count += 1  
                    
                    backtrack() 
                    
                    available[tile] += 1  
        
        backtrack()
        return count


                





        