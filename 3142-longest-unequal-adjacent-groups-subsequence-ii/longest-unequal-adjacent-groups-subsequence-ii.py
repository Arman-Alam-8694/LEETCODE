from typing import List
from functools import cache

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        def checkhamming(first, second):
            cnt = 0
            for i in range(len(first)):
                if second[i] != first[i]:
                    cnt += 1
                    if cnt > 1:
                        return False
            return cnt == 1  # exactly one difference

        @cache
        def recur(prev, curidx):
            if curidx == n:
                return []

            take = []
            skip = recur(prev, curidx + 1)

            if prev == -1:
                # Always valid to start a new sequence
                take = [words[curidx]] + recur(curidx, curidx + 1)
            elif len(words[prev]) == len(words[curidx]) and groups[prev] != groups[curidx]:
                if checkhamming(words[prev], words[curidx]):
                    take = [words[curidx]] + recur(curidx, curidx + 1)

            # Return the longer of take or skip
            if len(take) > len(skip):
                return take
            else:
                return skip

        return recur(-1, 0)
