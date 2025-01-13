class Solution:
    def minimumLength(self, s: str) -> int:
        array=[0]*26
        result=0
        for i in s:
            idx=ord(i)-ord("a")
            array[idx]+=1
        print(array)
        for i in array:
            if i:
                if i&1:
                    result+=i//2
                else:
                    result+=(i-1)//2
        return len(s)-(2*result)
        