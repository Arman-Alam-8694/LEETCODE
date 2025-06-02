class Solution:
    def candy(self, ratings: List[int]) -> int:
        #single pass O(n) solutin with constant space the problem with this question is 
        #i did miss some of edge cases like if there is increasing slope and then a decreasing
        #slope then the accumulated value of the increaseing slope we to take in account
        #because the next if decreasing slope  by greedy i can make it 1 but if n the future 
        #we get bigger decresing slope then i might need to change the accumulated value aswell 
        #because we are just maintain the start of the decreasing slope to track down the number
        # of elemeents you need add 1 to each but if the accumulated slope value is bigger 
        # than the number of elements in the decreasing slope then it's fine other wise we have to 
        #even change the accumulated value as well and also we are maintaing the prev value 
        #at each iteration and making it change value when we encounter the same rating becuase
        #[IMPORTANT]---if there is same rating then it doesn't matter if the next is smaller or bigger so we 
        #reset start here and also when we are about to start the increasing slope

        result=0
        start=None
        prev=1
        handle=0
        thandle=0
        for end in range(len(ratings)):
            if start is None:
                start=end
                result+=1
                prev=1
            elif ratings[end-1]==ratings[end]:
                result+=1
                start=end
                prev=1
                handle=None
            elif ratings[end-1]>ratings[end]:
                if prev>1:
                    result+=1
                    handle=prev
                    thandle=end-1
                    prev=1
                    start=end
                else:
                    calc=(end-start)+1
                    if handle and calc>=handle:
                        start=thandle
                        result+=(end-start)+1
                        handle=None
                    else:
                        result+=calc
                    prev=1

            elif ratings[end-1]<ratings[end]:
                prev=prev+1
                result+=prev
                start=end
                hanlde=None
            # print(f"current={end},start={start},result={result},rpev={prev}")
        return result


        