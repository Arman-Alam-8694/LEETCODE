class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # map={}
        # def recur(start):
        #     if start==len(questions)-1:
        #         return questions[start][0]
        #     if start>=len(questions):
        #         return 0
        #     if start in map:
        #         return map[start]
        #     map[start]=max(questions[start][0]+recur(start+questions[start][1]+1),recur(start+1))
        #     return map[start]
        # return recur(0)
        n=len(questions)
        dp=[0]*(n+1)

        for i in range(n-1,-1,-1):
            points,power=questions[i]
            next_idx=i+questions[i][1]+1
            take=points+dp[next_idx if next_idx <n else n]
            skip=dp[i+1]
            dp[i]=max(take,skip)
        return dp[0]
       