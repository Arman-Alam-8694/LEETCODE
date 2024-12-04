class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        alphabet="abcdefghijklmnopqrstuvwxyz"
        mapp={}
      
        s2=len(str2)
        a=len(alphabet)

        for i in range(a):
            mapp[alphabet[i]]=alphabet[(i+1)%a]

        left=0
        for char in str1:
            if char==str2[left]:
                left+=1
            elif mapp[char]==str2[left]:
                left+=1
            if left>=s2:
                return True
        return False

        