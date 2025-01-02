class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        class SegmentTree:
            def __init__(self, n):
                self.tree = [0] * (4 * n)
                self.n = n

            def build(self, arr, start, end, node):
                if start == end:
                    self.tree[node] = arr[start]
                    return
                mid = (start + end) // 2
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                self.build(arr, start, mid, left_child)
                self.build(arr, mid + 1, end, right_child)
                self.tree[node] = self.tree[left_child] + self.tree[right_child]

            def query(self, l, r, start, end, node):
                if r < start or l > end:
                    return 0
                if l <= start and r >= end:
                    return self.tree[node]
                mid = (start + end) // 2
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                left_sum = self.query(l, r, start, mid, left_child)
                right_sum = self.query(l, r, mid + 1, end, right_child)
                return left_sum + right_sum

        def is_vowel(c):
            return c in 'aeiou'

        def starts_and_ends_with_vowel(word):
            return is_vowel(word[0]) and is_vowel(word[-1])

        n = len(words)
        arr = [1 if starts_and_ends_with_vowel(word) else 0 for word in words]

        seg_tree = SegmentTree(n)
        seg_tree.build(arr, 0, n - 1, 0)

        ans = []
        for l, r in queries:
            ans.append(seg_tree.query(l, r, 0, n - 1, 0))
        return ans
