class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        
        if k==0:
            return [0]*n
        negative=False
        if k<0:
            k*=-1
            code=code[::-1]
            negative=True
        
        prefix_array=[]
      
        temp=0
        for i in range(2*n):
            temp+=code[(i%n)]
            prefix_array.append(temp)
        ans=[]
       
        for i in range(n):
            ans.append(prefix_array[i+k]-prefix_array[i])

        print(ans)
        if negative:
            return ans[::-1]
        
        return ans