class Solution:
    def maxDiff(self, num: int) -> int:
        temp=str(num)
        # mapp=Counter(temp)
        max_change=None
        min_change=None
        idx=0
        n=len(temp)
        to_change_one=False
        to_change_zero=False
        can_take_zero=False
        mapp=defaultdict(int)
        while idx<n:
            if max_change is None and temp[idx]!="9":
                max_change=temp[idx]
            if min_change is None:
                if temp[idx]!="0" and temp[0]!=temp[idx] and can_take_zero:
                    # print(mapp)
                    min_change=temp[idx]
                    to_change_zero=True
                elif temp[idx]!="1" and temp[idx]!="0":
                    min_change=temp[idx]
                    to_change_one=True
                else:
                    can_take_zero=True
            if max_change is not None and min_change is not None:
                break
            mapp[temp[idx]]+=1
            idx+=1
        print(min_change,max_change)
        max_number=""
        min_number=""
        for i in temp:
            if i==max_change:
                max_number+="9"
            else:
                max_number+=i
            if i==min_change:
                if to_change_zero:
                    min_number+="0"
                elif to_change_one:
                    min_number+="1"
            else:
                min_number+=i
        print(max_number, min_number)
        max_number=int(max_number)
        min_number=int(min_number)
        return max_number-min_number

        