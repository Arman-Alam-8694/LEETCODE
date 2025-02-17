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
                    available[i]-=1
                    if available[i]==0:
                        del available[i]
                    backtrack(cur_list,available,result)
                    if i in available:
                        available[i]+=1
                    else:
                        available[i]=1

        backtrack([],available,result)
        # print(result)
        return len(result)
                





        