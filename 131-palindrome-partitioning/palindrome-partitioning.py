class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        def check(s):
            if s[::-1]==s:
                return True
            return False
        result=[]
        path=[]
        def recur(idx,path):
            if idx==n:
                result.append(path.copy())
                return 
            for i in range(idx,n):
                if check(s[idx:i+1]):
                    path.append(s[idx:i+1])
                    recur(i+1,path)
                    path.pop()

        recur(0,path)
        return result
        