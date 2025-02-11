class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        part_size=len(part)
        for i in s:
            stack.append(i)
            if "".join(stack[-part_size:])==part:
                for i in range(part_size):
                    stack.pop()

        return "".join(stack)        