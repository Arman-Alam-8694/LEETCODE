class Solution:
    def maximumHappinessSum(self, happiness, k):
        def radix_sort(nums):
            if not nums:
                return nums

            max_val = max(nums)
            exp = 1  # 1, 10, 100, ...

            while max_val // exp > 0:
                count = [0] * 10
                output = [0] * len(nums)

                # Count digits
                for num in nums:
                    digit = (num // exp) % 10
                    count[digit] += 1

                # Prefix sum
                for i in range(1, 10):
                    count[i] += count[i - 1]

                # Stable placement (right to left)
                for i in range(len(nums) - 1, -1, -1):
                    digit = (nums[i] // exp) % 10
                    count[digit] -= 1
                    output[count[digit]] = nums[i]

                nums = output
                exp *= 10

            return nums

        happiness = radix_sort(happiness)

        ans = 0
        for i in range(k):
            val = happiness[-1 - i] - i
            if val <= 0:
                break
            ans += val

        return ans

