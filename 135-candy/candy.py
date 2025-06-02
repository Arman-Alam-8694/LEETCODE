class Solution:
    def candy(self, ratings: List[int]) -> int:
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


        