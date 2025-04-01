class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def recur(start):
            if start==len(questions)-1:
                return questions[start][0]
            if start>=len(questions):
                return 0
            return max(questions[start][0]+recur(start+questions[start][1]+1),recur(start+1))
        return recur(0)
       