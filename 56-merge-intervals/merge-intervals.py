class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        if n == 1:
            return arr
        result = [arr[0]]
        for next in range(1, n):
            if result[-1][1] >= arr[next][0]:
                nstart = result[-1][0]
                if result[-1][1] > arr[next][1]:
                    nend = result[-1][1]
                else:
                    nend = arr[next][1]
                new = [nstart, nend]
                if not result:
                    result.append(new)
                elif result and new[0] == result[-1][0]:
                    result.pop()
                    result.append(new)
                else:
                    result.append(new)
                arr[next] = new
            else:
                result.append(arr[next])
        return result
