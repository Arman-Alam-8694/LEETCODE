class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # --- Internal Helper: Two-Stack Min/Max Queue ---
        # We use lists as stacks. Each element is a tuple: (value, max_agg, min_agg)
        # This allows O(1) access to min/max without strictly tracking indices.
        in_stack = []
        out_stack = []

        def push(val):
            # When pushing to in_stack, we aggregate with the element below it
            cur_max = val
            cur_min = val
            if in_stack:
                cur_max = max(cur_max, in_stack[-1][1])
                cur_min = min(cur_min, in_stack[-1][2])
            in_stack.append((val, cur_max, cur_min))

        def pop():
            # If out_stack is empty, pour everything from in_stack (reversing order)
            if not out_stack:
                while in_stack:
                    val = in_stack.pop()[0]
                    # Re-calculate aggregation for out_stack perspective
                    cur_max = val
                    cur_min = val
                    if out_stack:
                        cur_max = max(cur_max, out_stack[-1][1])
                        cur_min = min(cur_min, out_stack[-1][2])
                    out_stack.append((val, cur_max, cur_min))
            
            # Now we can fast pop from the end
            if out_stack:
                out_stack.pop()

        def get_diff():
            # The window max/min is the extreme of both stacks combined
            mx = -float('inf')
            mn = float('inf')
            
            if in_stack:
                mx = max(mx, in_stack[-1][1])
                mn = min(mn, in_stack[-1][2])
            if out_stack:
                mx = max(mx, out_stack[-1][1])
                mn = min(mn, out_stack[-1][2])
                
            return mx - mn

        # --- Main DP Logic ---
        dp = [0] * (n + 1)
        dp[0] = 1
        
        # Prefix sum array for O(1) range sum queries
        # prefix_dp[i] stores sum(dp[0]...dp[i-1])
        prefix_dp = [0] * (n + 2)
        prefix_dp[1] = 1
        
        left = 0
        
        for right in range(n):
            push(nums[right])
            
            # If constraint violated, remove from the "virtual front" (using pop from stack end)
            while get_diff() > k:
                pop()
                left += 1
            
            # We need sum(dp[j]) for all valid start points j in [left, right]
            # This corresponds to prefix_dp[right+1] - prefix_dp[left]
            count = (prefix_dp[right + 1] - prefix_dp[left]) % MOD
            
            dp[right + 1] = count
            prefix_dp[right + 2] = (prefix_dp[right + 1] + count) % MOD
            
        return dp[n]