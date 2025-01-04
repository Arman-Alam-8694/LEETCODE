class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
            
        result = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # if first i chars form palindrome
                for rest in self.partition(s[i:]):  # recursively partition rest
                    result.append([s[:i]] + rest)
        return result