class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dictt = {}
        for i in nums:
            dictt[i] = []
            for j in nums:
                if j % i == 0 and j != i:
                    dictt[i].append(j)

        memo = {}

        def dfs(num):
            if num in memo:
                return memo[num]

            max_path = []
            for neighbor in dictt[num]:
                path = dfs(neighbor)
                if len(path) > len(max_path):
                    max_path = path

            memo[num] = [num] + max_path
            return memo[num]

        result = []
        for num in nums:
            path = dfs(num)
            if len(path) > len(result):
                result = path

        return result
