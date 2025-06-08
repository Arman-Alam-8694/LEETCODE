class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
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
