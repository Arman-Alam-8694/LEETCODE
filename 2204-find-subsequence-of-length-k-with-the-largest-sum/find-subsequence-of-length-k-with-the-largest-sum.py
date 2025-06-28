class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # result=float("-inf")
        # n=len(nums)
        # listt=[(nums[i],i) for i in range(n)]
        # listt.sort()
        # new=listt[n-k:]
        # new.sort(key=lambda x:x[1])
        # answer=[]
        # for i,j in new:
        #     answer.append(i)
        # return answer

      
        n = len(nums)
        
        # dp[j] = max sum of subsequence of length j
        prev = [float('-inf')] * (k + 1)
        prev[0] = 0
        
        # For traceback: (i, j) -> (prev_i, prev_j)
        trace = dict()
        
        for i in range(1, n + 1):
            curr = prev[:]
            for j in range(min(i, k), 0, -1):  # Go backward to avoid overwriting
                if prev[j - 1] + nums[i - 1] > curr[j]:
                    curr[j] = prev[j - 1] + nums[i - 1]
                    trace[(i, j)] = (i - 1, j - 1)
            prev = curr

        # Reconstruct subsequence from trace
        res = []
        i, j = n, k
        while j > 0:
            if (i, j) in trace:
                prev_i, prev_j = trace[(i, j)]
                res.append(nums[prev_i])
                i, j = prev_i, prev_j
            else:
                i -= 1  # Skip this index (was not selected)
        
        return res[::-1]  # reverse to restore correct order



            