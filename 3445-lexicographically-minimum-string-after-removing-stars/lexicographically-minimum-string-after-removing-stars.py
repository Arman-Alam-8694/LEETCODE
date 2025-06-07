#BETTER SOLUTION WITH o(N) 


# class Solution:
#     def clearStars(self, s: str) -> str:
#         char_idx=[[] for _ in range(27)]
#         n=len(s)
#         smallest=28
#         skip=set()
#         for i in range(n):
#             if s[i]=="*":
#                 skip.add(i)
   
#                 t=char_idx[smallest].pop()
#                 skip.add(t)
           
#                 if len(char_idx[smallest])==0:
#                     temp=smallest
#                     smallest=26
#                     for j in range(temp,26):
#                         if len(char_idx[j])>=1:
#                             smallest=j
#                             break
#             else:
#                 new=ord(s[i])-ord("a")
#                 if new<=smallest:
#                     smallest=new
#                 char_idx[new].append(i)
       
#         result=[]
#         for i in range(n):
#             if i not in skip:
#                 result.append(s[i])
#         return "".join(result)
        
class Solution:
    def clearStars(self, s: str) -> str:
        
        ans = list(s)
        heap = []
        

        for i, char in enumerate(s):
            if char == '*' and heap:
                del_char, j = heapq.heappop(heap)
                ans[-j] = ''
                ans[i] = ''
            else:
                heapq.heappush(heap, (char, -i))

        return ''.join(ans)