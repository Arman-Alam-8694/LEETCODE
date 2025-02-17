class Solution:
    
    def numTilePossibilities(self, tiles: str) -> int:
        unique_numbers=list(set(tiles))
        available=Counter(tiles)
   

        result=set()
        def backtrack(cur_list,available,result):
            if not available:
                return 
            for i in unique_numbers:
                if available[i]>0:
                    cur_list.append(i)
                    stringg="".join(cur_list)
                    if stringg not in result:
                        result.add(stringg)
                    # else:
                    #     return
                    available[i]-=1
                   
                    backtrack(cur_list,available,result)
                    available[i]+=1
                    cur_list.pop()
                 

        backtrack([],available,result)
        return len(result)
                





        