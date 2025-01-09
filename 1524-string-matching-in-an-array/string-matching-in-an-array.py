# class Solution:
#     def stringMatching(self, words: List[str]) -> List[str]:
#         result=[]
#         for i in range(len(words)):
#             for j in range(len(words)):
#                 if words[i] in words[j] and i!=j:
#                     result.append(words[i])
#                     break
#         return result

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        a = " ".join(words)
        return [w for w in words if a.count(w)>1]
        