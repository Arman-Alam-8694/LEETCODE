# class Solution:
#     def minimumDeletions(self, word: str, k: int) -> int:
#         freq=Counter(word)
#         listt=[i if i!=0 else None for i in freq.values()]
#         listt.sort()
#         n=len(listt)
#         prefix=[0]*(n+1)
#         for i in range(n):
#             prefix[i+1]=prefix[i]+listt[i]
#         answer=float("inf")
#         right=0
#         for left in range(n):
#             while right<n and listt[right]-listt[left]<=k:
#                 right+=1
#             left_discard=prefix[left]
#             right_part=prefix[n]-prefix[right]
#             adjust=right_part-(listt[left]+k)*(n-right)
#             answer=min(answer,left_discard+adjust)


#         return answer
    
from collections import Counter
from bisect import bisect_right

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        listt = list(freq.values())
        listt.sort()
        n = len(listt)

        # Compute prefix sum of sorted frequencies
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + listt[i]

        answer = float('inf')
        for left in range(n):
            # Find the first index where listt[right] > listt[left] + k
            threshold = listt[left] + k
            right = bisect_right(listt, threshold)

            # Deletions on the left of current group
            left_discard = prefix[left]
            # Elements to adjust on the right to reduce their count to threshold
            right_part = prefix[n] - prefix[right]
            adjust = right_part - (threshold * (n - right))
            
            # Update minimum answer
            answer = min(answer, left_discard + adjust)

        return answer
