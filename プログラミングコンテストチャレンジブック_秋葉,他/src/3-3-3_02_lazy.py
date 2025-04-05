# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_G&lang=jp
# 


class LazySegmentTree:
    def __init__(self, length):
        self.length = 1<<(length-1).bit_length()
        self.tree = [0] * (2 * self.length)
        self.lazy = [0] * (2 * self.length)

    def _push(self, node, l, r):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if r - l > 1:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def _add(self, a, b, val, node, l, r):
        self._push(node, l, r)
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.lazy[node] += val
            self._push(node, l, r)
        else:
            m = (l + r) // 2
            self._add(a, b, val, node * 2, l, m)
            self._add(a, b, val, node * 2 + 1, m, r)
            self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])

    # b : exclusive
    def add(self, a, b, val):
        self._add(a, b, val, 1, 0, self.length)


    def _query_min(self, a, b, node, l, r):
        self._push(node, l, r)
        if b <= l or r <= a:
            return float('inf')
        if a <= l and r <= b:
            return self.tree[node]
        else:
            m = (l + r) // 2
            left = self._query_min(a, b, node * 2, l, m)
            right = self._query_min(a, b, node * 2 + 1, m, r)
            return min(left, right)

    # b : exclusive
    def query_min(self, a, b):
        return self._query_min(a, b, 1, 0, self.length)
    


n, q = map(int, input().split())

st = LazySegmentTree(n)

for _ in range(q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        s, t = query[1:]
        print(st.query_min(s, t+1))
    else:
        s, t, x = query[1:]
        st.add(s, t+1, x)    
        # print(st.data)




