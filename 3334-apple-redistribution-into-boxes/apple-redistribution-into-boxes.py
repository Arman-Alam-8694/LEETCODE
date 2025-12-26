class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total=sum(apple)
        temp=0
        for i in range(len(capacity)):
            temp+=capacity[i]
            if temp>=total:
                return i+1
        return i+1

        