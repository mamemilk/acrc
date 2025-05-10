# https://atcoder.jp/contests/s8pc-2/tasks/s8pc_2_h
# 
# 遅延評価Segment Treeで反転の有無を覚える。

class LazySegmentTree:
    def __init__(self, length):
        self.logn = ((length - 1).bit_length())
        self.n = 1 << self.logn
        self.tree = [0] * (2 * self.n + 1)
        self.lazy = [0] * (2 * self.n + 1)

    def propagate(self, node, node_left, node_right):
        if self.lazy[node] % 2 == 1:
            self.tree[node] = (node_right - node_left + 1) - self.tree[node]
            if node < self.n:
                self.lazy[node * 2] ^= 1
                self.lazy[node * 2 + 1] ^= 1
        self.lazy[node] = 0

    def update_range(self, l, r):
        self._update_range(1, 0, self.n - 1, l, r)

    def _update_range(self, node, node_left, node_right, l, r):
        self.propagate(node, node_left, node_right)
        if r < node_left or node_right < l:
            return
        if l <= node_left and node_right <= r:
            self.lazy[node] ^= 1
            self.propagate(node, node_left, node_right)
        # node_left no migi hashi 
        node_middle = (node_left + node_right)// 2
        if node_left == node_right:
            return        
        self._update_range(node * 2, node_left, node_middle, l, r)
        self._update_range(node * 2 + 1, node_middle + 1, node_right, l, r)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query_range(self, l, r):# r is inclusive
        return self._query_range(1, 0, self.n - 1, l, r)

    def _query_range(self, node, node_left, node_right, l, r): 
        self.propagate(node, node_left, node_right)
        if r < node_left or node_right < l:
            return 0
        if l <= node_left and node_right <= r:
            return self.tree[node]
        mid = (node_left + node_right) // 2
        left_sum = self._query_range(node * 2, node_left, mid, l, r)
        right_sum = self._query_range(node * 2 + 1, mid + 1, node_right, l, r)
        return left_sum + right_sum
    

n, Q = map(int, input().split())

seg = LazySegmentTree(n)
for _ in range(Q):
    q, l, r = map(int, input().split())

    if q == 1:
        seg.update_range(l, r)
    else:
        print(seg.query_range(l, r))

        