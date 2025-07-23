class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pattern(s, a, b, score):
            stack = []
            total = 0
            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    total += score
                else:
                    stack.append(ch)
            return ''.join(stack), total
        
        if x >= y:
            s, score1 = remove_pattern(s, 'a', 'b', x)
            _, score2 = remove_pattern(s, 'b', 'a', y)
        else:
            s, score1 = remove_pattern(s, 'b', 'a', y)
            _, score2 = remove_pattern(s, 'a', 'b', x)
        
        return score1 + score2
