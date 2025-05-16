# class Solution:
#     def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
#         n=len(words)
#         def checkhamming(first,second):
#             cnt=0
            
#             for i in range(len(first)):
#                 if second[i]!=first[i]:
#                     cnt+=1
#                 if cnt>1:
#                     return False
#             return True
#         result=[]
#         @cache
#         def recur(prev,curidx):
#             take=[]
#             if curidx==n:
#                 return []
#             skip=recur(prev,curidx+1)
#             if prev==-1:
#                 take=[words[curidx]]+recur(curidx,curidx+1)
               
#             elif len(words[prev])==len(words[curidx]):
#                 check=checkhamming(words[prev],words[curidx])
#                 if check and groups[prev]!=groups[curidx]:
#                     take=[words[curidx]]+recur(curidx,curidx+1)
            
#             if len(take)>len(skip):
#                 return take
#             else:
#                 return skip

#         return recur(-1,0)

from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        def checkhamming(first, second):
            cnt = 0
            for i in range(len(first)):
                if first[i] != second[i]:
                    cnt += 1
                    if cnt > 1:
                        return False
            return cnt == 1

        dp = [1] * n              # dp[i] = longest subsequence ending at i
        prev_idx = [-1] * n       # to reconstruct path

        for i in range(n):
            for j in range(i):
                if len(words[i]) == len(words[j]) and groups[i] != groups[j] and checkhamming(words[i], words[j]):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev_idx[i] = j

        # Reconstruct longest path
        max_len = max(dp)
        idx = dp.index(max_len)

        res = []
        while idx != -1:
            res.append(words[idx])
            idx = prev_idx[idx]

        return res[::-1]  # reverse to get correct order

        