class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        #recusive but takes extra space not ideal

        # result=[]
        # def dfs(num):
        #     if num>n:
        #         return 
        #     result.append(num)
        #     for i in range(10):
        #         temp=num*10
        #         temp+=i
        #         dfs(temp)

        # for k in range(1,10):
        #     dfs(k)
        # return result
        result=[]
        start=1
        for _ in range(n):
            result.append(start)
            if start*10<=n:
                start=start*10
            else:
                while start%10==9 or start==n:
                    start=start//10
                start+=1
        return result
