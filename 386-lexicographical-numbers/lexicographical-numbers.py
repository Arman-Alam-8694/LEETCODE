class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result=[]
        def dfs(num):
            if num>n:
                return 
            result.append(num)
            for i in range(10):
                temp=num*10
                temp+=i
                dfs(temp)

        for k in range(1,10):
            dfs(k)
        return result


