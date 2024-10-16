class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = sorted([('a', a), ('b', b), ('c', c)], key=lambda x: -x[1])
        result = []
        
        while True:
            for i, (char, count) in enumerate(chars):
                if count == 0:
                    continue
                if len(result) >= 2 and result[-1] == result[-2] == char:
                    continue
                result.append(char)
                chars[i] = (char, count - 1)
                break
            else:
                break
            
            chars.sort(key=lambda x: -x[1])
        
        return ''.join(result)