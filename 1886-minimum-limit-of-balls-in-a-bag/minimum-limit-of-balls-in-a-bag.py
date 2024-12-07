class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        u = sum(nums)
        b = maxOperations
        splits = [max(n*b//u, 1) for n in nums]
        heap = [(-1 * ((n+split-1)//split), n, split) for n, split in zip(nums, splits)]
        heapq.heapify(heap)
        for _ in range(maxOperations + len(nums) - sum(splits)):
            item = heapq.heappop(heap)
            _, n, split = item
            num = (n+split)//(split+1)
            heapq.heappush(heap, (-num, n, split+1))
        return - heap[0][0]