# class Solution:
#     def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # n=len(differences)

        #find the valid sequence such that the max element is least as possible it can be
        #achieved starting with smallest pair 
        #then take the max of it and do 1+(upper-maxx) because
        #the differences of the sequence is same so if we increase each array element upto to maxx
        #then again the difference will be same so that's why 
        #we try to find the smallest valid sequence 
        #which is not optimal but passes the test cases
        #maybe due to pruning and all but still the run time is very bad

        # def recur(idx,prev,maxx):
        #     if idx==n:
        #         return True,maxx
        #     ahead=differences[idx]+prev
        #     if lower<=ahead<=upper :
        #         temp=max(maxx,ahead)
        #         correct,answer=recur(idx+1,ahead,temp)
        #         if correct:
        #             return True,answer
        #         else:
        #             return False,0
        #     return False,0

        # for i in range(lower,upper+1):
        #     ahead=differences[0]+i
        #     if lower<=ahead<=upper:
        #         maxx=max(i,ahead)
        #         correct,ans=recur(1,ahead,maxx)
        #         if correct:
        #             return 1+(upper-ans)
        # return 0

        # prefix=0
        # minn=0
        # maxx=0
        # for d in differences:
        #     prefix+=d
        #     minn=min(prefix,minn)
        #     maxx=max(prefix,maxx)
        #     if maxx-minn>upper-lower:
        #         return 0
        # return (upper-maxx)+(minn-lower)+1

                   
                
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)

        for start in range(lower, upper + 1):
            curr = start
            maxx = start
            valid = True

            for diff in differences:
                curr += diff
                if not (lower <= curr <= upper):
                    valid = False
                    break
                maxx = max(maxx, curr)

            if valid:
                return 1 + (upper - maxx)

        return 0









        