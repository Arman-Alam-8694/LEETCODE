from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort by x descending, then y ascending (mirror of original)
        points.sort(key=lambda p: (-p[0], p[1]))
        ans = 0
        n = len(points)

        for j in range(n):                  # left → right over the mirrored order
            y = points[j][1]
            mny = float("inf")              # track the smallest yy we've counted so far
            for i in range(j + 1, n):       # look to the "right" (smaller x)
                yy = points[i][1]
                # Mirror of: if (yy >= mny || yy < y) continue;
                if yy < y or yy >= mny:
                    continue
                ans += 1
                mny = yy
        return ans
