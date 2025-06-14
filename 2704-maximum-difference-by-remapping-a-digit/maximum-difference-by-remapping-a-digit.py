class Solution:
    def minMaxDifference(self, num: int) -> int:
        temp=str(num)
        max_change=None
        min_change=None
        idx=0
        n=len(temp)
        while idx<n:
            if max_change is None and temp[idx]!="9":
                max_change=temp[idx]
            if min_change is None and temp[idx]!="0":
                min_change=temp[idx]
            if max_change is not None and min_change is not None:
                break
            idx+=1
        max_number=""
        min_number=""
        for i in temp:
            if i==max_change:
                max_number+="9"
            else:
                max_number+=i
            if i==min_change:
                min_number+="0"
            else:
                min_number+=i
        print(max_number, min_number)
        max_number=int(max_number)
        min_number=int(min_number)
        return max_number-min_number

        