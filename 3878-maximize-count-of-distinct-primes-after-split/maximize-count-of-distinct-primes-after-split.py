MX = 100_001
is_p = [True] * MX
is_p[0] = is_p[1] = False
for i in range(2, MX):
    if is_p[i]:
        for j in range(i * i, MX, i):
            is_p[j] = False


class Node:
    __slots__ = 'val', 'todo'

class LazySegmentTree:
    # 懒标记初始值
    _TODO_INIT = 0

    def __init__(self, n: int, init_val=0):
        # 线段树维护一个长为 n 的数组（下标从 0 到 n-1），元素初始值为 init_val
        # init_val 可以是 list 或者 int
        # 如果是 int，那么创建一个 list
        if isinstance(init_val, int):
            init_val = [init_val] * n
        self._n = n
        self._tree = [Node() for _ in range(2 << (n - 1).bit_length())]
        self._build(init_val, 1, 0, n - 1)

    # 合并两个 val
    def _merge_val(self, a: int, b: int) -> int:
        return a if a > b else b

    # 把懒标记作用到 node 子树（本例为区间加）
    def _apply(self, node: int, l: int, r: int, todo: int) -> None:
        cur = self._tree[node]
        # 计算 tree[node] 区间的整体变化
        cur.val += todo
        cur.todo += todo

    # 把当前节点的懒标记下传给左右儿子
    def _spread(self, node: int, l: int, r: int) -> None:
        todo = self._tree[node].todo
        if todo == self._TODO_INIT:  # 没有需要下传的信息
            return
        m = (l + r) // 2
        self._apply(node * 2, l, m, todo)
        self._apply(node * 2 + 1, m + 1, r, todo)
        self._tree[node].todo = self._TODO_INIT  # 下传完毕

    # 合并左右儿子的 val 到当前节点的 val
    def _maintain(self, node: int) -> None:
        self._tree[node].val = self._merge_val(self._tree[node * 2].val, self._tree[node * 2 + 1].val)

    # 用 a 初始化线段树
    # 时间复杂度 O(n)
    def _build(self, a: List[int], node: int, l: int, r: int) -> None:
        self._tree[node].todo = self._TODO_INIT
        if l == r:  # 叶子
            self._tree[node].val = a[l]  # 初始化叶节点的值
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)  # 初始化左子树
        self._build(a, node * 2 + 1, m + 1, r)  # 初始化右子树
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, ql: int, qr: int, f: int) -> None:
        if ql <= l and r <= qr:  # 当前子树完全在 [ql, qr] 内
            self._apply(node, l, r, f)
            return
        self._spread(node, l, r)
        m = (l + r) // 2
        if ql <= m:  # 更新左子树
            self._update(node * 2, l, m, ql, qr, f)
        if qr > m:  # 更新右子树
            self._update(node * 2 + 1, m + 1, r, ql, qr, f)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:  # 当前子树完全在 [ql, qr] 内
            return self._tree[node].val
        self._spread(node, l, r)
        m = (l + r) // 2
        if qr <= m:  # [ql, qr] 在左子树
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:  # [ql, qr] 在右子树
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(l_res, r_res)

    # 用 f 更新 [ql, qr] 中的每个 a[i]
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def update(self, ql: int, qr: int, f: int) -> None:
        self._update(1, 0, self._n - 1, ql, qr, f)

    # 返回用 _merge_val 合并所有 a[i] 的计算结果，其中 i 在闭区间 [ql, qr] 中
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)


class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        pos = defaultdict(SortedList)
        for i, x in enumerate(nums):
            if is_p[x]:
                pos[x].add(i)

        t = LazySegmentTree(n, 0)
        for sl in pos.values():
            if len(sl) > 1:
                t.update(sl[0], sl[-1], 1)

        def update(sl: SortedList, i: int, delta: int) -> None:
            l, r = sl[0], sl[-1]
            if l == r:
                t.update(min(l, i), max(r, i), delta)
            elif i < l:
                t.update(i, l - 1, delta)
            elif i > r:
                t.update(r + 1, i, delta)

        ans = []
        for i, val in queries:
            old = nums[i]
            nums[i] = val

            # 处理旧值
            if is_p[old]:
                sl = pos[old]
                sl.remove(i)
                if sl:
                    update(sl, i, -1)
                else:
                    del pos[old]

            # 处理新值
            if is_p[val]:
                sl = pos[val]
                if sl:
                    update(sl, i, 1)
                sl.add(i)

            # 整个数组的不同质数个数 + 切一刀的最大额外收益
            ans.append(len(pos) + t.query(0, n - 1))

        return ans