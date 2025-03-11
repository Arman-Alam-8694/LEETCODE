# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         n=len(s)
#         # left=0
#         # Found=False
#         # sett={}
#         result=0
#         lasta=None
#         lastb=None
#         lastc=None
#         # for right in range(n):
#         #     if Found:
#         #         if s[right] not in sett:
#         #             sett[s[right]]=0
#         #         sett[s[right]]+=1
#         #         if s[left]==s[right]:
#         #             while left<right:
#         #                 sett[s[left]]-=1
#         #                 if sett[s[left]]==0:
#         #                     sett[s[left]]+=1
#         #                     break
#         #                 left+=1
#         #         result+=(left-(-1))
    
#         #     else:
#         #         if s[right] not in sett:
#         #             sett[s[right]]=0
#         #         sett[s[right]]+=1
#         #         if len(sett)==3:
#         #             while left<right:
#         #                 sett[s[left]]-=1
#         #                 if sett[s[left]]==0:
#         #                     sett[s[left]]+=1
#         #                     break
#         #                 left+=1
#         #             result+=(left-(-1))
#         #             Found=True

        # for right in range(n):
        #     if s[right]=="a":
        #         lasta=right
        #     elif s[right]=="b":
        #         lastb=right
        #     else:
        #         lastc=right
        #     if lasta is not None and lastb is not None and lastc is not None:
        #         temp=min(lasta,lastb,lastc)
        #         result+=temp+1


        # return result


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lasta,lastb,lastc=None,None,None
        result = 0
        
        for right, char in enumerate(s):
            if char=="a":
                lasta=right
            elif char=="b":
                lastb=right
            else:
                lastc=right
            if None not in (lasta,lastb,lastc):
                result += min(lasta,lastb,lastc) + 1  # Count valid substrings
            
        return result
