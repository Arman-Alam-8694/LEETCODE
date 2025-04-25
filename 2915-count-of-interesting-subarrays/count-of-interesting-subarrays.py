class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        def helper(l, r):
            if l == r:
                cnt = 1 if (nums[l] % modulo == k) else 0
                return 1 if (cnt % modulo == k) else 0
            
            mid = (l + r) // 2
            left_count = helper(l, mid)
            right_count = helper(mid + 1, r)
            cross_count = count_cross(l, mid, r)
            return left_count + right_count + cross_count
    
        def count_cross(l, mid, r):
            # Compute prefix counts for left half (l..mid)
            prefix = []
            cnt = 0
            for i in range(mid, l - 1, -1):  # left to mid (backwards)
                if nums[i] % modulo == k:
                    cnt += 1
                prefix.append(cnt % modulo)
            
            # Compute suffix counts for right half (mid+1..r)
            suffix = []
            cnt = 0
            for i in range(mid + 1, r + 1):  # mid+1 to right
                if nums[i] % modulo == k:
                    cnt += 1
                suffix.append(cnt % modulo)
            
            # Count (prefix[i] + suffix[j]) % modulo == k
            from collections import defaultdict
            prefix_counts = defaultdict(int)
            for p in prefix:
                prefix_counts[p] += 1
            
            cross = 0
            for s in suffix:
                desired = (k - s) % modulo
                cross += prefix_counts.get(desired, 0)
            return cross
        
        return helper(0, len(nums) - 1)
            