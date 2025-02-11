class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        part_size=len(part)
        for i in s:
            stack.append(i)
            if i==part[-1]:
                if stack[-part_size:]==list(part):
                    for i in range(part_size):
                        stack.pop()

        return "".join(stack)        