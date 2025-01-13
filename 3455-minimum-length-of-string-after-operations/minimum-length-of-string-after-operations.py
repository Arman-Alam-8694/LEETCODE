class Solution:
    def minimumLength(self, s: str) -> int:
        # array=[0]*26
        # result=0
        # for i in s:
        #     idx=ord(i)-ord("a")
        #     array[idx]+=1
        # print(array)
        # for i in array:
        #     if i:
        #         if i&1:
        #             result+=i//2
        #         else:
        #             result+=(i-1)//2
        # return len(s)-(2*result)


        mapp=Counter(s)
        result=0
        for k,v in mapp.items():
            if v&1:
                result+=1
            else:
                result+=2
        return result

        # mapp=defaultdict(int)
        # result=0
        # for i in s:
        #     mapp[i]+=1
        #     if mapp[i]==3:
        #         result+=1
        #         mapp[i]-=2
        # return len(s)-(2*result)

        # s_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        # ans = 0
        # for ch in s_set:
        #     count = s.count(ch)
        #     if count & 1:
        #         ans += 1
        #     elif count != 0:
        #         ans += 2
        # return ans


        