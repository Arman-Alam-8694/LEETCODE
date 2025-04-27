class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        # bad=-1
        # minn=-1
        # maxx=-1
        # res=0
        # for right in range(len(nums)):
        #     if nums[right]==minK:
        #         minn=right
        #     if nums[right]==maxK:
        #         maxx=right
        #     elif not minK<=nums[right]<=maxK:
        #         bad=right
        #     if minn!=-1 and maxx!=-1:
        #         # print(min(0,min(minn,maxx)-bad))
        #         res+=max(0,min(minn,maxx)-bad)
        # return res
        n = len(nums)
    
        # First pass: left to right - get nearest previous bad index
        prev_bad = [-1] * n
        last_invalid = -1
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                last_invalid = i
            prev_bad[i] = last_invalid

        # Second pass: right to left - get nearest next bad index
        next_bad = [n] * n
        last_invalid = n
        for i in range(n-1, -1, -1):
            if nums[i] < minK or nums[i] > maxK:
                last_invalid = i
            next_bad[i] = last_invalid

        ans = 0
        last_minK = -1
        last_maxK = -1
        
        for i in range(n):
            if nums[i] == minK:
                last_minK = i
            if nums[i] == maxK:
                last_maxK = i

            # The window must be fully inside valid range
            left_bound = max(prev_bad[i],  -1)
            right_bound = min(next_bad[i], n)

            # Find minimum position where both minK and maxK appeared
            valid_pos = min(last_minK, last_maxK)

            # Count valid subarrays ending at i
            if valid_pos > left_bound:
                ans += valid_pos - left_bound

        return ans




