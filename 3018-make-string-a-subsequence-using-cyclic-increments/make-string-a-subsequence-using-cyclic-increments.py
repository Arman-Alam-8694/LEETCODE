class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        left=0
        s2=len(str2)
        if len(str1)==len(str2):
            for charr in str1:
                if (charr==str2[left]) or (chr(ord(charr)+1)==str2[left]) or (str2[left]=="a" and charr=="z"):
                    left+=1
                else:
                    return False
            return True
   
        for charr in str1:
            if (charr==str2[left]) or (chr(ord(charr)+1)==str2[left]) or (str2[left]=="a" and charr=="z"):
                left+=1
            if left>=s2:
                return True
        return False

        