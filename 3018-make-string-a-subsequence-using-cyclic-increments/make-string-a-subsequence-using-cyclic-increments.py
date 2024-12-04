class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s2=len(str2)
        left=0
        for charr in str1:
            if (charr==str2[left]) or (chr(ord(charr)+1)==str2[left]) or (str2[left]=="a" and charr=="z"):
                left+=1
            if left>=s2:
                return True
        return False

        