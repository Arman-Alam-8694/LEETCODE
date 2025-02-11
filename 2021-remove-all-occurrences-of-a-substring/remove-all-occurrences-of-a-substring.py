class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        part_size=len(part)
        for i in s:
            stack.append(i)
            if len(stack)>=part_size and stack[-part_size:]==list(part):
                    del stack[-part_size:]

        return "".join(stack)        