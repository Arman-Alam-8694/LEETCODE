class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        result=[]
        path=[]
        def recur(idx,path):
            if idx==n:
                result.append(path.copy())
                return 
            for i in range(idx,n):
                if s[idx:i+1][::-1]==s[idx:i+1]:
                    path.append(s[idx:i+1])
                    recur(i+1,path)
                    path.pop()

        recur(0,path)
        return result
        