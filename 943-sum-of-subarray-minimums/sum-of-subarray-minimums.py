class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod=10**9+7

        # 3
        # 3 1-[1,3]
        # 3 1 2-[1,3]
        # 3 1 2 4-[1,3]

        # 3 1 2 4
        # 3+1+1=4
        # 4+2

        # 1 2 3 4 4 4  3
        presum=0
        result=0
        n=len(arr)
        stack=[]
        for i in range(n):
            curr=arr[i]
            last=i
            while stack and stack[-1][0]>curr:
                last_element,tlast=stack.pop()
                presum-=(last-tlast)*last_element
                last=tlast
            # print("before:",presum)
            stack.append((curr,last))
            newmiddle=(i-last)*curr
            presum+=curr+newmiddle
            # print("after:",presum)
            result+=presum
            # print(result)
          
        return result%mod

        