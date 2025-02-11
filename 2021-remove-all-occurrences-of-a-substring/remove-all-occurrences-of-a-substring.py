class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        part_size=len(part)
        for i in s:
            stack.append(i)
            if i==part[-1] and len(stack)>=part_size:
                
                if stack[-part_size:]==list(part):
                    del stack[-part_size:]

        return "".join(stack)        